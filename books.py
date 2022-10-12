from enum import Enum
from mimetypes import init



class Book:
    def __init__(self, id, title, desc) -> None:
        self.id = id
        self.title = title
        self.desc = desc


book_manager = {
        "1": Book("1","testBook", "Here is a test book, it eventually will have lots of descriptive information!"),
        "2": Book("2","testBook", "Here is a test book, it eventually will have lots of descriptive information!"),
        "3": Book("3","testBook", "Here is a test book, it eventually will have lots of descriptive information!"),
        "4": Book("4","testBook", "Here is a test book, it eventually will have lots of descriptive information!"),
        "5": Book("5","testBook", "Here is a test book, it eventually will have lots of descriptive information!"),
        "6": Book("6","testBook", "Here is a test book, it eventually will have lots of descriptive information!"),
    }