from actions.game_actions import ChangePlayerLocationAction

from ui.ui import UI, Button


class MapUI(UI):
    def __init__(self, section,  x, y, tiles):
        super().__init__(section, x, y)

        bd = [4, 4, 6, 1]  # Button Dimensions
        button_tiles = tiles[bd[0]:bd[0] + bd[2], bd[1]:bd[1] + bd[3]]
        left_button = Button(x=bd[0], y=bd[1], width=bd[2],height=bd[3], click_action=ChangePlayerLocationAction(self.section.engine, "client"), tiles=button_tiles)
        self.add_element(left_button)

        bd = [4, 5, 10, 1]  # Button Dimensions
        button_tiles = tiles[bd[0]:bd[0] + bd[2], bd[1]:bd[1] + bd[3]]
        left_button = Button(x=bd[0], y=bd[1], width=bd[2],height=bd[3], click_action=ChangePlayerLocationAction(self.section.engine, "bloomsbury"), tiles=button_tiles)
        self.add_element(left_button)
