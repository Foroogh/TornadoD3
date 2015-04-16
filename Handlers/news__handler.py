import tornado
import peewee
from models import *

__author__ = 'Forough'
__project__ = 'TornadoD3'


class NewsHandler(tornado.web.RequestHandler):
    def get(self):
        news = News.select()
        self.render('news.html', news=news)


class NewsEditHandler(tornado.web.RequestHandler):
    def get(self, *args):
        news_id = args[0]
        news_info = News.select().where(News.id == news_id).get()
        self.render("news-edit.html", news=news_info)

    def post(self, *args):
        news_id = args[0]
        news_info = News.select().where(News.id == news_id).get()

        news_info.name = self.get_argument("news-name")
        news_info.save()
        self.redirect("/news")


class NewsDeleteHandler(tornado.web.RequestHandler):
    def get(self, *args):
        news_id = args[0]
        news_info = News.select().where(News.id == news_id).get().delete_instance()
        self.redirect("/news")


class NewsNewHandler(tornado.web.RequestHandler):
    def get(self, *args):
        self.render("news-new.html")

    def post(self, *args):
        news_name = self.get_argument("news-name")
        news_info = News.create(name=news_name)

        self.redirect("/news")