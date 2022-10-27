from actions.game_actions import (DisplayCurrentLocationAction,
                                  DisplayCurrentSublocationAction,
                                  DisplayMapAction)

from ui.ui import UI, Button


class NavUI(UI):
    def __init__(self, section,  x, y, tiles):
        super().__init__(section, x, y)
        self.tiles = tiles

    def setup_nav_buttons(self):
        self.elements.clear()

        if self.section.engine.are_currently_at_sublocation():
            bd = [1, 0, 12, 4] 
            button_tiles = self.tiles[bd[0]:bd[0] + bd[2], bd[1]:bd[1] + bd[3]]
            left_button = Button(x=bd[0], y=bd[1], width=bd[2],height=bd[3], click_action=DisplayCurrentSublocationAction(self.section.engine), tiles=button_tiles)
            self.add_element(left_button)

        bd = [13, 0, 8, 4]
        button_tiles = self.tiles[bd[0]:bd[0] + bd[2], bd[1]:bd[1] + bd[3]]
        left_button = Button(x=bd[0], y=bd[1], width=bd[2],height=bd[3], click_action=DisplayCurrentLocationAction(self.section.engine), tiles=button_tiles)
        self.add_element(left_button)

        bd = [21, 0, 8, 4]
        button_tiles = self.tiles[bd[0]:bd[0] + bd[2], bd[1]:bd[1] + bd[3]]
        left_button = Button(x=bd[0], y=bd[1], width=bd[2],height=bd[3], click_action=DisplayMapAction(self.section.engine), tiles=button_tiles)
        self.add_element(left_button)


