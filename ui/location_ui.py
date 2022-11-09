from actions.actions import OpenConfirmationDialog
from actions.game_actions import ChangePlayerSublocationAction, SearchLocationAction

from ui.ui import UI, Tooltip, Button, Input
from books import book_manager
from sections.section_layouts import location_screen_info


class LocationUI(UI):
    def __init__(self, section,  x, y, tiles):
        super().__init__(section, x, y)
        self.tiles = tiles

    def setup_sublocation_buttons(self, x, y, y_gap, sublocations, button_mask):
        count = 0
        for sublocation in sublocations:
            if not sublocation.hidden:
                sublocation_name = sublocation.name            
                bd = [x, y + ( y_gap * count),location_screen_info["button_width"], location_screen_info["button_height"]]  # Button Dimensions
                b = Button(x=bd[0], y=bd[1], width=bd[2], height=bd[3], click_action=OpenConfirmationDialog(
                self.section.engine, "Travel to {0}?".format(sublocation_name), ChangePlayerSublocationAction(self.section.engine, sublocation_name), self.section.name, enable_ui_on_confirm=False),h_fg=location_screen_info["b_h_color"])
                b.set_mask(button_mask)
                self.add_element(b)
                count += 1

    def setup_search_bar(self, location_name):
        search_bar = Input(location_screen_info["search_bar"]["x"],location_screen_info["search_bar"]["y"],location_screen_info["search_bar"]["width"],location_screen_info["search_bar"]["height"], SearchLocationAction(self.section.engine,self.section, location_name))
        self.add_element(search_bar)