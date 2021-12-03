import os
import jinja2
import webapp2
import re

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


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class MainPage(Handler):
    def get(self):
        self.response.out.write("Hello, Udacity!")


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


class WelcomeHandler(Handler):
    def get(self):
        username = self.request.get("username")
        if valid_username("username"):
            self.render("welcome.html", username=username)
        else:
            self.redirect("/unit2/signup")


app = webapp2.WSGIApplication([("/", MainPage),
                               ("/unit2/rot13", ROT13Handler),
                               ("/unit2/signup", SignupHandler),
                               ("/unit2/welcome", WelcomeHandler)],
                              debug=True)
