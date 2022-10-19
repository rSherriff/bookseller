from actions.actions import OpenConfirmationDialog
from actions.game_actions import PurchaseBook

from ui.ui import UI, Tooltip, Button
from books import book_manager


class ShopUI(UI):
    def __init__(self, section,  x, y, tiles):
        super().__init__(section, x, y)
        self.tiles = tiles

    def setup_book_tooltips(self, x, y, y_gap, book_ids):
        count = 0
        for id in book_ids:
            book = book_manager[id]
            t = Tooltip(x,y + ( y_gap * count), len("x: " + book.title), 1, book.desc)
            self.add_element(t)
            count += 1

    def setup_book_buttons(self, x, y, y_gap, shop_name, book_ids):
        count = 0
        for id in book_ids:
            book = book_manager[id]
            bd = [x, y + ( y_gap * count), 3, 1]  # Button Dimensions
            button_tiles = self.tiles[bd[0]:bd[0] + bd[2], bd[1]:bd[1] + bd[3]]
            b = Button(x=bd[0], y=bd[1], width=bd[2], height=bd[3], click_action=OpenConfirmationDialog(
            self.section.engine, "Purchase this book?", PurchaseBook(self.section.engine, shop_name, book), self.section.name), tiles=button_tiles)
            self.add_element(b)
            count += 1
