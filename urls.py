__author__ = 'mojtaba.banaie'

from Handlers.index_handler import IndexHandler
from Handlers.category__handler import CategoryHandler, CategoryEditHandler, CategoryDeleteHandler, CategoryNewHandler
from Handlers.author__handler import AuthorHandler, AuthorEditHandler, AuthorDeleteHandler, AuthorNewHandler

urlList = [
    (r'/', IndexHandler),

    (r'/category$', CategoryHandler),
    (r'/category/edit/(\d+)$', CategoryEditHandler),
    (r'/category/delete/(\d+)$', CategoryDeleteHandler),
    (r'/category/new$', CategoryNewHandler),

    (r'/author$', AuthorHandler),
    (r'/author/edit/(\d+)$', AuthorEditHandler),
    (r'/author/delete/(\d+)$', AuthorDeleteHandler),
    (r'/author/new$', AuthorNewHandler)
]
