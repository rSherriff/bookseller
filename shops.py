from enum import Enum
from mimetypes import init
from books import *



class Shop:
    def __init__(self, name) -> None:
        self.name = name
        self.stock = Stock(self.name)

segap = Shop("Segap")

shop_manager = {
    segap.name: segap
}