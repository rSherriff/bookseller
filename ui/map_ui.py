from actions.actions import OpenConfirmationDialog
from actions.game_actions import ChangePlayerLocationAction, OpenChangePlayerLocationConfirmationAction

from ui.ui import UI, Button


class MapUI(UI):
    def __init__(self, section,  x, y, tiles):
        super().__init__(section, x, y)
        self.tiles = tiles

    def setup_location_buttons(self, locations):
        self.elements.clear()
        for location in locations:
            bd = [location[1],location[2],location[3],location[4]]  # Button Dimensions
            button_tiles = self.tiles[bd[0]:bd[0] + bd[2], bd[1]:bd[1] + bd[3]]
            left_button = Button(x=bd[0], y=bd[1], width=bd[2],height=bd[3], click_action=OpenChangePlayerLocationConfirmationAction(
                self.section.engine, "Travel to {0}?".format(location[0]), location[0],ChangePlayerLocationAction(self.section.engine, location[0]), self.section.name, enable_ui_on_confirm=False), tiles=button_tiles)
            self.add_element(left_button)        
