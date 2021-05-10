import os
import jinja2
import webapp2
from google.appengine.ext import db


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir), autoescape=True)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render(self, template, **kw):
        self.write(render_str(template, **kw))

def blog_key(name = 'default'):
    return db.Key.from_path('blogs', name)

class Blog(db.Model):
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)

    def render(self):
        self._render_text = self.content.replace('\n', '<br>')
        return render_str("post.html", p = self)

class MainPage(Handler):
    def render_front(self, subject="", content="", error=""):
        blogs = db.GqlQuery("SELECT * FROM Blog ORDER BY created DESC;")
        self.render("blog.html", blogs=blogs)

    def get(self):
        self.render_front()

class PostPage(Handler):
    def get(self,post_id):
        key = db.Key.from_path("Blog",int(post_id),parent=blog_key())
        post = db.get(key)

        if not post:
            self.error(404)
            return
        self.render("permalink.html",post=post)

class NewPostPage(Handler):
    def get(self):
        self.render("newpost.html")

    def post(self):
        subject = self.request.get("subject")
        content = self.request.get("content")
        if subject and content:
            a = Blog(parent = blog_key(),subject=subject, content=content)
            a.put()
            ##########################
            self.redirect("/blog/%s" % str(a.key().id()))
            ##########################
        else:
            error = "subject and content, please!"
            self.render("newpost.html", subject=subject,
                        content=content, error=error)
app = webapp2.WSGIApplication([("/blog/?", MainPage),
                               ("/blog/newpost", NewPostPage),
                               ("/blog/([0-9]+)", PostPage)], debug=True)
