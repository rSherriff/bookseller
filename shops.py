from enum import Enum
from mimetypes import init
from books import *



class Shop:
    def __init__(self, name) -> None:
        self.name = name
        self.stock = Stock(self.name)

segap = Shop("Segap")
segap.stock.add_book(book_manager["1"])
segap.stock.add_book(book_manager["2"])
segap.stock.add_book(book_manager["3"])
segap.stock.add_book(book_manager["rosacrucian"])
segap.stock.add_book(book_manager["5"])
segap.stock.add_book(book_manager["6"])

hs = Shop("hidden_shop")

shop_manager = {
    segap.name: segap,
    hs.name : hs
}