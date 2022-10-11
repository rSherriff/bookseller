from enum import Enum
from mimetypes import init
from books import books



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

class ShopManager():
    def __init__(self) -> None:

        skoob = Shop("Skoob")
        skoob.add_book(books["1"])

        self.shops = {
            "skoob": skoob
        }