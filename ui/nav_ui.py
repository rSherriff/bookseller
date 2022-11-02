from actions.game_actions import (DisplayCurrentLocationAction,
                                  DisplayCurrentSublocationAction,
                                  DisplayMapAction)

from ui.ui import UI, Button, Tooltip


class NavUI(UI):
    def __init__(self, section,  x, y, tiles):
        super().__init__(section, x, y)
        self.tiles = tiles

    def setup_nav_buttons(self):
        self.elements.clear()

        bd = [1, 0, 12, 4] 
        if self.section.engine.are_currently_at_sublocation():
            left_button = Button(x=bd[0], y=bd[1], width=bd[2],height=bd[3], click_action=DisplayCurrentSublocationAction(self.section.engine))
            self.add_element(left_button)
        else:
            tooltip_text = "You are not currently at a location!"
            t = Tooltip(x=bd[0], y=bd[1], width=bd[2], height=bd[3]-2, text=tooltip_text)
            self.add_element(t)

        bd = [13, 0, 8, 4]
        left_button = Button(x=bd[0], y=bd[1], width=bd[2],height=bd[3], click_action=DisplayCurrentLocationAction(self.section.engine))
        self.add_element(left_button)

        bd = [21, 0, 8, 4]
        left_button = Button(x=bd[0], y=bd[1], width=bd[2],height=bd[3], click_action=DisplayMapAction(self.section.engine))
        self.add_element(left_button)


