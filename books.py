from enum import Enum
from mimetypes import init



class Book:
    def __init__(self, id, title, desc) -> None:
        self.id = id
        self.title = title
        self.desc = desc


books = {
        "1": Book("1","testBook", "Here is a test book, it eventually will have of descriptive information!"),
    }