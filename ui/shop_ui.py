from actions.actions import OpenConfirmationDialog
from actions.game_actions import PurchaseBook

from ui.ui import UI, Tooltip, Button
from books import book_manager
from sections.section_layouts import shop_screen_info


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

    def setup_book_buttons(self, x, y, y_gap, shop_name, book_ids,button_mask):
        count = 0
        for id in book_ids:
            book = book_manager[id]
            bd = [x, y + ( y_gap * count), shop_screen_info["button_width"], shop_screen_info["button_height"]]  # Button Dimensions
            b = Button(x=bd[0], y=bd[1], width=bd[2], height=bd[3], click_action=OpenConfirmationDialog(
            self.section.engine, "Purchase this book?", PurchaseBook(self.section.engine, shop_name, book), self.section.name),h_fg=shop_screen_info["b_h_color"])
            b.set_mask(button_mask)
            self.add_element(b)
            count += 1
