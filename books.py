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

    def items(self):
        return self.stock.items()



book_manager = {
        "1": Book("1","Ogdoas Scholastica", "A heavy foolscap octavo. The fronitspiece is a city on a hill."),
        "6": Book("6","Theatrum philosophicum", "A rough, buckram bound book.  The frontispiece depicts an eight-sided church tower above the date 1676"),
        "2": Book("2","Lexicon philosophicum", "A book bound in old calf. Dated 1632."),
        "3": Book("3","Metaphysicae systema methodicum", "The fortispiece claims this book is the work of Christian Rosencrantz. It is dated 1653."),
        "rosacrucian": Book("rosacrucian","The Sacred Marriage", "A small book dated 1627. The frontispiece depicts an eight-sided church tower above the word 'Fecit'."),
        "5": Book("5","Simplicius Simplicissimus", "A poorly bound quatro, you have to hold the pages in. Sine loco, anno, vel nomine"),
    }