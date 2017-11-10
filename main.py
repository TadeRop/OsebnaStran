#!/usr/bin/env python
import os
import jinja2
import webapp2
import random

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("index.html")

class OmeniHandler(BaseHandler):
    def get(self):
        return self.render_template("omeni.html")


class MojiprojektiHandler(BaseHandler):
    def get(self):
        return self.render_template("mojiprojekti.html")

class BlogHandler(BaseHandler):
    def get(self):
        sporocilo = "To je moje sporocilo"

        blog_posts = [{"title": "Prvi blog", "text": "test"}, {"title": "Drugi blog", "text": "test2"}, {"title": "Tretji blog", "text": "test3"}]

        params = {"sporocilo": sporocilo, "blogs": blog_posts}

        return self.render_template("blog.html", params=params)

class KontaktHandler(BaseHandler):
    def get(self):
        return self.render_template("kontakt.html")

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/Omeni', OmeniHandler),
    webapp2.Route('/Mojiprojekti', MojiprojektiHandler),
    webapp2.Route('/Blog', BlogHandler),
        webapp2.Route('/Kontakt', KontaktHandler),
], debug=True)
