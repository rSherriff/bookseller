from enum import Enum
from mimetypes import init
from books import *



class Shop:
    def __init__(self, name) -> None:
        self.name = name
        self.stock = Stock(self.name)

skoob = Shop("Skoob")
skoob.stock.add_book(book_manager["1"])
skoob.stock.add_book(book_manager["2"])
skoob.stock.add_book(book_manager["3"])
skoob.stock.add_book(book_manager["4"])
skoob.stock.add_book(book_manager["5"])
skoob.stock.add_book(book_manager["6"])

shop_manager = {
    skoob.name: skoob
}