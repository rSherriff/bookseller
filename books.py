from enum import Enum
from mimetypes import init



class Book:
    def __init__(self, id, title, desc) -> None:
        self.id = id
        self.title = title
        self.desc = desc

class Stock:
    def __init__(self, name) -> None:
        self.name = name
        self.stock = {}

    def add_book(self, book):
        self.stock[book.id] = book
        print("Added {0} - {1} to {2}'s stock".format(book.id, book.title, self.name))

    def remove_book(self, book):
        remove_key = self.stock.pop(book.id, None)

        if remove_key != None:
            print("Removed {0} - {1} from {2}'s stock".format(book.id, book.title, self.name))
            return True
        else:
            print("Failed to remove {0} - {1} from {2}'s stock".format(book.id, book.title, self.name))
            return False

    def get_book_ids(self):
        return self.stock.keys()

    def values(self):
        return self.stock.values()



book_manager = {
        "1": Book("1","testBook", "Here is a test book, it eventually will have lots of descriptive information!"),
        "2": Book("2","testBook", "Here is a test book, it eventually will have lots of descriptive information!"),
        "3": Book("3","testBook", "Here is a test book, it eventually will have lots of descriptive information!"),
        "4": Book("4","testBook", "Here is a test book, it eventually will have lots of descriptive information!"),
        "5": Book("5","testBook", "Here is a test book, it eventually will have lots of descriptive information!"),
        "6": Book("6","testBook", "Here is a test book, it eventually will have lots of descriptive information!"),
    }