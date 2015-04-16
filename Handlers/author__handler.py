import tornado
import peewee
from models import *

__author__ = 'Forough'
__project__ = 'PoemMaker'


class AuthorHandler(tornado.web.RequestHandler):
    def get(self):
        authors = Author.select()
        self.render('authors.html', authors=authors)


class AuthorNewHandler(tornado.web.RequestHandler):
    def get(self, *args):
        self.render("author-new.html")

    def post(self, *args):
        sur_name = self.get_argument("author-forename")
        last_name = self.get_argument("author-surname")
        aut_info = Author.create(
            fn=sur_name,
            ln=last_name
        )
        self.redirect("/author")


class AuthorEditHandler(tornado.web.RequestHandler):
    def get(self, *args):
        aut_id = args[0]
        aut_info = Author.select().where(Author.id == aut_id).get()
        self.render("author-edit.html", author=aut_info)

    def post(self, *args):
        aut_id = args[0]
        aut_info = Author.select().where(Author.id == aut_id).get()

        aut_info.fn = self.get_argument("author-forename")
        aut_info.ln = self.get_argument("author-surname")
        aut_info.save()
        self.redirect("/author")


class AuthorDeleteHandler(tornado.web.RequestHandler):
    def get(self, *args):
        aut_id = args[0]
        News.delete().where(News.author == aut_id).execute()
        aut_info = Author.select().where(Author.id == aut_id).get().delete_instance()
        self.redirect("/author")