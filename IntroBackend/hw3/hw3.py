import os
import jinja2
import webapp2
import re
import hashlib
import hmac
import random
import string
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir), autoescape=True)

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PWD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")


def valid_username(username):
    return username and USER_RE.match(username)


def valid_password(password):
    return password and PWD_RE.match(password)


def valid_email(email):
    return not email or EMAIL_RE.match(email)


def make_secure_val(s):
    return "%s|%s" % (s, hmac.new("SECRET", s).hexdigest())


def check_secure_val(h):
    s, HASH = h.split("|")
    return s if make_secure_val(s) == h else None


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def set_secure_cookie(self, name, val):
        cookie_val = make_secure_val(val)
        self.response.headers.add_header(
            "Set-Cookie", "%s=%s; Path=/" % (name, cookie_val))

    def read_secure_cookie(self, name):
        cookie_val = self.request.cookies.get(name)
        return cookie_val and check_secure_val(cookie_val)

    def login(self, user):
        self.set_secure_cookie("user_id", str(user.key().id()))

    def logout(self):
        self.response.headers.add_header("Set-Cookie", "user_id=; Path=/")

    def initialize(self, *a, **kw):
        webapp2.RequestHandler.initialize(self, *a, **kw)
        uid = self.read_secure_cookie("user_id")
        self.user = uid and User.by_id(int(uid))


def make_salt(length=5):
    return "".join([random.choice(string.ascii_letters) for _ in range(length)])


def make_pw_hash(name, pw, salt=None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name+pw+salt).hexdigest()
    return "%s,%s" % (salt, h)


def valid_pw(name, password, h):
    salt = h.split(",")[0]
    return h == make_pw_hash(name, password, salt)


def users_key(group="default"):
    return db.Key.from_path("users", group)


class User(db.Model):
    name = db.StringProperty(required=True)
    pw_hash = db.StringProperty(required=True)
    email = db.StringProperty()

    @classmethod
    def by_id(cls, uid):
        return User.get_by_id(uid, parent=users_key())

    @classmethod
    def by_name(cls, name):
        u = User.all().filter("name =", name).get()
        return u

    @classmethod
    def register(cls, name, pw, email=None):
        pw_hash = make_pw_hash(name, pw)
        return User(parent=users_key(), name=name, pw_hash=pw_hash, email=email)

    @classmethod
    def login(cls, name, pw):
        u = cls.by_name(name)
        if u and valid_pw(name, pw, u.pw_hash):
            return u


class MainPage(Handler):
    def get(self):
        self.response.out.write("Hello, Udacity!")


class SignupHandler(Handler):
    def get(self):
        self.render("Signup.html")

    def post(self):
        has_error = False
        self.username = self.request.get("username")
        self.password = self.request.get("password")
        self.verify = self.request.get("verify")
        self.email = self.request.get("email")
        params = {}
        params["usr"], params["pwd"] = "", ""

        if not valid_username(self.username):
            has_error = True
            params["usr"] = "That's not a valid username."
        if not valid_password(self.password):
            has_error = True
            params["pwd"] = "That wasn't a valid password."
        elif self.password != self.verify:
            has_error = True
            params["verify"] = "Your passwords didn't match."

        if not valid_email(self.email):
            has_error = True
            params["email"] = "That's not a valid email."

        if has_error:
            self.render("Signup.html", **params)
        else:
            self.done()

    def done(self, *a, **kw):
        raise NotImplementedError


class Register(SignupHandler):
    def done(self):
        u = User.by_name(self.username)
        if u:
            msg = "That user already exists."
            self.render("Signup.html", usr=msg)
        else:
            u = User.register(self.username, self.password, self.email)
            u.put()

            self.login(u)
            self.redirect("/unit3/welcome")


class Login(Handler):
    def get(self):
        self.render("login-form.html")

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        u = User.login(username, password)
        if u:
            self.login(u)
            self.redirect("/unit3/welcome")
        else:
            msg = "Invalid login"
            self.render("login-form.html", error=msg)


class Logout(Handler):
    def get(self):
        self.logout()
        self.redirect("/signup")


class Unit3Welcome(Handler):
    def get(self):
        if self.user:
            self.render("welcome.html", username=self.user.name)
        else:
            self.redirect("/signup")


app = webapp2.WSGIApplication([("/", MainPage),
                               ("/signup", Register),
                               ("/login", Login),
                               ("/logout", Logout),
                               ("/unit3/welcome", Unit3Welcome)],
                              debug=True)
