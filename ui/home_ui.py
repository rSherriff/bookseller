from actions.game_actions import OpenAdvanceDayConfirmationAction, AdvanceDayAction

from ui.ui import UI, Button
from sections.section_layouts import home_screen_info

class HomeUI(UI):
    def __init__(self, section,  x, y, tiles):
        super().__init__(section, x, y)
        self.tiles = tiles

        x = home_screen_info["advance_day_btn"]["x"]
        y = home_screen_info["advance_day_btn"]["y"]
        width = home_screen_info["advance_day_btn"]["width"]
        height = home_screen_info["advance_day_btn"]["height"]

        button_tiles = self.tiles[x:x+width,y:y+height]
        b = Button(x=x, y=y, width=width, height=height, click_action=OpenAdvanceDayConfirmationAction(
        self.section.engine, "Advance the day?", AdvanceDayAction(self.section.engine), self.section.name, enable_ui_on_confirm=True), tiles=button_tiles)
        self.add_element(b)
