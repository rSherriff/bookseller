import json
from collections import OrderedDict
from enum import Enum, auto
from threading import Timer
from unicodedata import name

from pygame import mixer

from books import *
from engine import Engine, GameState
from locations import *
from sections.client_section import ClientSection
from sections.confirmation import Confirmation
from sections.home_section import HomeSection
from sections.info_section import InfoSection
from sections.intro_section import IntroSection
from sections.map_section import MapSection
from sections.nav_section import NavSection
from sections.notification import Notification
from sections.shop_section import ShopSection
from shops import *


class MainSectionState(Enum):
    NONE = auto(),
    LOCATION = auto(),
    MAP = auto(),

class PlayerState:
    def __init__(self) -> None:
        self.day = 0
        self.location = "home"


class Game(Engine):
    def __init__(self, teminal_width: int, terminal_height: int):
        super().__init__(teminal_width, terminal_height)

        self.player = PlayerState()

        self.main_section_state = MainSectionState.NONE

        self.display_current_location()

    def create_new_save_data(self):
        pass

    def load_initial_data(self, data):
        pass

    def load_fonts(self):
        pass

    def setup_sections(self):
        self.disabled_sections = []
        self.disabled_ui_sections = []

        self.intro_sections = OrderedDict()
        self.intro_sections["introSection"] = IntroSection(self,0,0,self.screen_width, self.screen_height)

        self.menu_sections = OrderedDict()

        self.game_sections = OrderedDict()
        self.game_sections["clientSection"] = ClientSection(self, 0,0, self.screen_width, self.screen_height)
        self.game_sections["mapSection"] = MapSection(self, 0,0, self.screen_width, self.screen_height)
        self.game_sections["shopSection"] = ShopSection(self, 0,0, self.screen_width, self.screen_height)
        self.game_sections["homeSection"] = HomeSection(self, 0,0, self.screen_width, self.screen_height)
        self.game_sections["navSection"] = NavSection(self, 0,self.screen_height - 10, self.screen_width, 10)
        self.game_sections["infoSection"] = InfoSection(self, self.screen_width - 15,0, 15, self.screen_height - 10)
        
        self.misc_sections = OrderedDict()
        self.misc_sections["notificationDialog"] = Notification(self, 7, 9, 37, 10)
        self.misc_sections["confirmationDialog"] = Confirmation(self, 7, 9, 37, 10)

        self.completion_sections = OrderedDict()

        self.disabled_sections = ["confirmationDialog", "notificationDialog", "mapSection", "shopSection", "clientSection", "homeSection"]
        self.disabled_ui_sections = ["confirmationDialog", "notificationDialog"]

    def display_map(self):
        self.close_all_main_sections()
        self.enable_section("mapSection")
        self.change_main_section_state(MainSectionState.MAP)

    def display_current_location(self):
        self.display_location(self.player.location)

    def display_location(self, location):
        if self.main_section_state == MainSectionState.LOCATION:
            return

        print(("Changing to location {0}").format(location))
        location = location_manager[location]

        self.close_all_main_sections()

        if location.type == LocationType.CLIENT:
            self.enable_section("clientSection") 
        elif location.type == LocationType.SHOP:
            self.enable_section("shopSection")
            self.game_sections["shopSection"].setup(location)
        elif location.type == LocationType.HOME:
            self.enable_section("homeSection")

        self.change_main_section_state(MainSectionState.LOCATION)

    def close_all_main_sections(self):
        self.game_sections["shopSection"].close()
        self.game_sections["mapSection"].close()
        self.game_sections["homeSection"].close()
        self.game_sections["clientSection"].close()

        self.disable_section("shopSection")
        self.disable_section("mapSection")
        self.disable_section("homeSection")
        self.disable_section("clientSection")


    def change_player_location(self, location):
        if not location == self.player.location:
            self.player.location = location
            self.display_current_location()

    def change_main_section_state(self, new_state):
        self.main_section_state = new_state
        
