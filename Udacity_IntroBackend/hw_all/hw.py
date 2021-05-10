import os
import jinja2
import re
import webapp2
from google.appengine.ext import db
import random
import string
import hmac
import hashlib


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir), autoescape=True)


def blog_key(name='default'):
    return db.Key.from_path('blogs', name)


def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)


""" Base class """


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render(self, template, **kw):
        self.write(render_str(template, **kw))

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


class MainPage(Handler):
    def get(self):
        self.response.out.write("Hello, Udacity!")


""" HW1 """
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PWD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")


def valid_username(username):
    return username and USER_RE.match(username)


def valid_password(password):
    return password and PWD_RE.match(password)


def valid_email(email):
    return not email or EMAIL_RE.match(email)


class ROT13Handler(Handler):
    def get(self):
        self.render("ROT13.html")

    def post(self):
        text = self.request.get("text")
        ROT13_text = ""
        for i in range(len(text)):
            if text[i].isalpha():
                if text[i].islower():
                    ROT13_text += chr(ord('a') +
                                      (ord(text[i]) - ord('a') + 13) % 26)
                elif text[i].isupper():
                    ROT13_text += chr(ord('A') +
                                      (ord(text[i]) - ord('A') + 13) % 26)
            else:
                ROT13_text += text[i]
        self.render("ROT13.html", ROT13_text=ROT13_text)


class SignupHandler(Handler):
    def get(self):
        self.render("Signup.html")

    def post(self):
        has_error = False
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")
        params = {}
        params["usr"], params["pwd"] = "", ""

        if not valid_username(username):
            has_error = True
            params["usr"] = "That's not a valid username."
        if not valid_password(password):
            has_error = True
            params["pwd"] = "That wasn't a valid password."
        elif password != verify:
            has_error = True
            params["verify"] = "Your passwords didn't match."

        if not valid_email(email):
            has_error = True
            params["email"] = "That's not a valid email."

        if has_error:
            self.render("Signup.html", **params)
        else:
            self.redirect("/unit2/welcome?username="+username)

    def done(self, *a, **kw):
        raise NotImplementedError


class WelcomeHandler(Handler):
    def get(self):
        username = self.request.get("username")
        if valid_username("username"):
            self.render("welcome.html", username=username)
        else:
            self.redirect("/unit2/signup")


""" HW2 """


class Blog(db.Model):
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)

    def render(self):
        self._render_text = self.content.replace('\n', '<br>')
        return render_str("post.html", p=self)


class BlogMainPage(Handler):
    def get(self, subject="", content="", error=""):
        blogs = db.GqlQuery("SELECT * FROM Blog ORDER BY created DESC;")
        self.render("blog.html", blogs=blogs)


class PostPage(Handler):
    def get(self, post_id):
        key = db.Key.from_path("Blog", int(post_id), parent=blog_key())
        post = db.get(key)

        if not post:
            self.error(404)
            return
        self.render("permalink.html", post=post)


class NewPostPage(Handler):
    def get(self):
        self.render("newpost.html")

    def post(self):
        subject = self.request.get("subject")
        content = self.request.get("content")
        if subject and content:
            a = Blog(parent=blog_key(), subject=subject, content=content)
            a.put()
            ##########################
            self.redirect("/blog/%s" % str(a.key().id()))
            ##########################
        else:
            error = "subject and content, please!"
            self.render("newpost.html", subject=subject,
                        content=content, error=error)


""" HW3 """


def make_secure_val(s):
    return "%s|%s" % (s, hmac.new("SECRET", s).hexdigest())


def check_secure_val(h):
    s, HASH = h.split("|")
    return s if make_secure_val(s) == h else None


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


class Register(SignupHandler):
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
                               ("/unit2/rot13", ROT13Handler),
                               ("/unit2/signup", SignupHandler),
                               ("/unit2/welcome", WelcomeHandler),
                               ("/blog/?", BlogMainPage),
                               ("/blog/newpost", NewPostPage),
                               ("/blog/([0-9]+)", PostPage),
                               ("/signup", Register),
                               ("/login", Login),
                               ("/logout", Logout),
                               ("/unit3/welcome", Unit3Welcome)], debug=True)
