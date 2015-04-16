from os import abort
import tornado
import peewee
from models import *

__author__ = 'Forough'
__project__ = 'TornadoD3'


class NewsHandler(tornado.web.RequestHandler):
    def get(self):
        news = News.select()
        self.render('news.html', allnews=news)


class NewsNewHandler(tornado.web.RequestHandler):
    def get(self, *args):
        self.render("news-new.html")

    def post(self, *args):
        news_author_id = self.get_argument("news-author-id")
        news_category_id = self.get_argument("news-category-id")
        news_body = self.get_argument("news-body")
        news_date = self.get_argument("news-date")
        news_title = self.get_argument("news-title")
        try:
         #   assert isinstance(news_body, object)
            news_info = News.create(
                author=news_author_id,
                category=news_category_id,
                body=news_body,
                title=news_title,
                date=news_date
            )
        except:
            abort(404)
        self.redirect("/news")


class NewsEditHandler(tornado.web.RequestHandler):
    def get(self, *args):
        news_id = args[0]
        news_info = News.select().where(News.id == news_id).get()
        self.render("news-edit.html", news=news_info)

    def post(self, *args):
        news_id = args[0]
        news_info = News.select().where(News.id == news_id).get()

        news_info.body = self.get_argument("news-body")
        news_info.date = self.get_argument("news-date")
        news_info.title = self.get_argument("news-title")
        news_info.save()
        self.redirect("/news")


class NewsDeleteHandler(tornado.web.RequestHandler):
    def get(self, *args):
        news_id = args[0]
        news_info = News.select().where(News.id == news_id).get().delete_instance()
        self.redirect("/news")
