from actions.game_actions import SearchMuseumAction

from ui.ui import UI, Input
from books import book_manager
from sections.section_layouts import museum_screen_info


class MuseumUI(UI):
    def __init__(self, section,  x, y, tiles):
        super().__init__(section, x, y)
        self.tiles = tiles

    def setup_search_bar(self):
        search_bar = Input(museum_screen_info["search_bar"]["x"],museum_screen_info["search_bar"]["y"],museum_screen_info["search_bar"]["width"],museum_screen_info["search_bar"]["height"], SearchMuseumAction(self.section.engine, self.section))
        self.add_element(search_bar)