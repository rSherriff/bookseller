from actions.game_actions import DisplayCurrentLocationAction, DisplayMapAction

from ui.ui import UI, Button


class NavUI(UI):
    def __init__(self, section,  x, y, tiles):
        super().__init__(section, x, y)

        bd = [4, 4, 8, 1]  # Button Dimensions
        button_tiles = tiles[bd[0]:bd[0] + bd[2], bd[1]:bd[1] + bd[3]]
        left_button = Button(x=bd[0], y=bd[1], width=bd[2],height=bd[3], click_action=DisplayCurrentLocationAction(self.section.engine), tiles=button_tiles)
        self.add_element(left_button)

        bd = [17, 4, 3, 1]  # Button Dimensions
        button_tiles = tiles[bd[0]:bd[0] + bd[2], bd[1]:bd[1] + bd[3]]
        left_button = Button(x=bd[0], y=bd[1], width=bd[2],height=bd[3], click_action=DisplayMapAction(self.section.engine), tiles=button_tiles)
        self.add_element(left_button)
