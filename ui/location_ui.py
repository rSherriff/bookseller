from actions.actions import OpenConfirmationDialog
from actions.game_actions import ChangePlayerSublocationAction

from ui.ui import UI, Tooltip, Button
from books import book_manager


class LocationUI(UI):
    def __init__(self, section,  x, y, tiles):
        super().__init__(section, x, y)
        self.tiles = tiles

    def setup_sublocation_buttons(self, x, y, y_gap, sublocation_names):
        count = 0
        for sublocation_name in sublocation_names:
            bd = [x, y + ( y_gap * count), 2, 1]  # Button Dimensions
            b = Button(x=bd[0], y=bd[1], width=bd[2], height=bd[3], click_action=OpenConfirmationDialog(
            self.section.engine, "Travel to {0}?".format(sublocation_name), ChangePlayerSublocationAction(self.section.engine, sublocation_name), self.section.name, enable_ui_on_confirm=False))
            self.add_element(b)
            count += 1
