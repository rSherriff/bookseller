from actions.game_actions import ChangePlayerLocationAction

from ui.ui import UI, Tooltip
from books import book_manager


class ShopUI(UI):
    def __init__(self, section,  x, y, tiles):
        super().__init__(section, x, y)

    def setup_book_tooltips(self, x, y, y_gap, book_ids):
        count = 0
        for id in book_ids:
            book = book_manager[id]
            t = Tooltip(x,y + ( y_gap * count), len(book.title), 1, book.desc)
            self.add_element(t)
            count += 1
