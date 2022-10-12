from enum import Enum
from mimetypes import init
from books import *



class Shop:
    def __init__(self, name) -> None:
        self.name = name
        self.stock = {}

    def add_book(self, book):
        self.stock[book.id] = book

    def remove_book(self, book):
        remove_key = self.stock.pop(book.id, None)

        if remove_key != None:
            print("Removed {0} - {1} from {2}'s stock".format(book.id, book.title, self.name))
        else:
            print("Failed to remove {0} - {1} from {2}'s stock".format(book.id, book.title, self.name))

    def get_book_ids(self):
        ids = []
        for key in self.stock.keys():
            ids.append(key)
        return ids

skoob = Shop("Skoob")
skoob.add_book(book_manager["1"])
skoob.add_book(book_manager["2"])
skoob.add_book(book_manager["3"])
skoob.add_book(book_manager["4"])
skoob.add_book(book_manager["5"])
skoob.add_book(book_manager["6"])

shop_manager = {
    "skoob": skoob
}