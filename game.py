import json
from collections import OrderedDict
from datetime import date, datetime, timedelta
from enum import Enum, auto
from sqlite3 import Date
from threading import Timer
from unicodedata import name
from xmlrpc.client import DateTime

from pygame import mixer

from books import *
from books import Stock
from engine import CONFIRMATION_DIALOG, NOTIFICATION_DIALOG, Engine, GameState
from locations import *
from sections.client_section import ClientSection
from sections.confirmation import Confirmation
from sections.home_section import HomeSection
from sections.info_section import InfoSection
from sections.intro_section import IntroSection
from sections.location_section import LocationSection
from sections.map_section import MapSection
from sections.nav_section import NavSection
from sections.notification import Notification
from sections.shop_section import ShopSection
from shops import *
from utils.definitions import TravelStatus

game_rules = {
    "LocationTravelTimeIncrement" : 1,
    "SublocationTravelTimeIncrement": 0,
    "DayEndHour" : 18
}

INTRO_SECTION = "introSection"
MAP_SECTION = "mapSection"
CLIENT_SECTION = "clientSection"
SHOP_SECTION = "shopSection"
HOME_SECTION = "homeSection"
LOCATION_SECTION = "locationSection"
NAV_SECTION = "navSection"
INFO_SECTION = "infoSection"

class MainSectionState(Enum):
    NONE = auto(),
    LOCATION = auto(),
    SUBLOCATION = auto(),
    MAP = auto(),

class PlayerState:
    def __init__(self) -> None:
        self.name = "Player"
        self.location = "Home"
        self.sublocation = "Home"
        self.stock = Stock("PInv")

class TimeState:
    def __init__(self) -> None:
        self.dt = datetime(1983,4,13,12)

    def increment_day(self):
        self.dt += timedelta(day=1)
        self.dt.hour = 0

    def get_hour(self):
        return self.dt.hour

    def get_date_string(self):
        return self.dt.strftime("%a - %d/%m/%y")

    def get_hour_string(self):
        return self.dt.strftime("%H:%M")

    def increment_time(self, hours):
        self.dt += timedelta(hours=hours)

class Game(Engine):
    def __init__(self, teminal_width: int, terminal_height: int):
        super().__init__(teminal_width, terminal_height)

        self.player = PlayerState()
        self.time = TimeState()

        self.main_section_state = MainSectionState.NONE

        self.display_current_sublocation()

    def create_new_save_data(self):
        pass

    def load_initial_data(self, data):
        pass

    def load_fonts(self):
        pass

    #*********************************************
    # Sections
    #*********************************************

    def setup_sections(self):
        self.disabled_sections = []
        self.disabled_ui_sections = []

        self.intro_sections = OrderedDict()
        self.intro_sections[INTRO_SECTION] = IntroSection(self,0,0,self.screen_width, self.screen_height, INTRO_SECTION)

        self.menu_sections = OrderedDict()

        self.game_sections = OrderedDict()
        self.game_sections[CLIENT_SECTION] = ClientSection(self, 0,0, self.screen_width, self.screen_height, CLIENT_SECTION)
        self.game_sections[MAP_SECTION] = MapSection(self, 0,0, self.screen_width, self.screen_height, MAP_SECTION)
        self.game_sections[SHOP_SECTION] = ShopSection(self, 0,0, self.screen_width, self.screen_height, SHOP_SECTION)
        self.game_sections[HOME_SECTION] = HomeSection(self, 0,0, self.screen_width, self.screen_height, HOME_SECTION)
        self.game_sections[LOCATION_SECTION] = LocationSection(self, 0,0, self.screen_width, self.screen_height, LOCATION_SECTION)
        self.game_sections[NAV_SECTION] = NavSection(self, 0,self.screen_height - 10, self.screen_width, 10, NAV_SECTION)
        self.game_sections[INFO_SECTION] = InfoSection(self, self.screen_width - 15,0, 15, self.screen_height - 10, INFO_SECTION)
        
        
        self.misc_sections = OrderedDict()
        self.misc_sections[NOTIFICATION_DIALOG] = Notification(self, 7, 9, 37, 10, NOTIFICATION_DIALOG)
        self.misc_sections[CONFIRMATION_DIALOG] = Confirmation(self, 7, 9, 37, 10, CONFIRMATION_DIALOG)

        self.completion_sections = OrderedDict()

        self.disabled_sections = [CONFIRMATION_DIALOG, NOTIFICATION_DIALOG, MAP_SECTION, SHOP_SECTION, CLIENT_SECTION, HOME_SECTION, LOCATION_SECTION]
        self.disabled_ui_sections = [CONFIRMATION_DIALOG, NOTIFICATION_DIALOG]

    def close_all_main_sections(self):
        self.game_sections[SHOP_SECTION].close()
        self.game_sections[MAP_SECTION].close()
        self.game_sections[HOME_SECTION].close()
        self.game_sections[CLIENT_SECTION].close()
        self.game_sections[LOCATION_SECTION].close()

        self.disable_section(SHOP_SECTION)
        self.disable_section(MAP_SECTION)
        self.disable_section(HOME_SECTION)
        self.disable_section(CLIENT_SECTION)
        self.disable_section(LOCATION_SECTION)

    #*********************************************
    # Locations
    #*********************************************

    def display_current_location(self):
        self.display_location(self.player.location)
    
    def display_current_sublocation(self):
        self.display_sublocation(self.player.location, self.player.sublocation)

    def display_location(self, location):
        self.player.sublocation = "none"
        self.close_all_main_sections()
        self.enable_section(LOCATION_SECTION)
        self.game_sections[LOCATION_SECTION].open(location)
        print(("Changing to location {0}").format(location))
        self.change_main_section_state(MainSectionState.LOCATION)

    def display_sublocation(self, location, sublocation):
        if self.main_section_state == MainSectionState.SUBLOCATION:
            print("WARNING! - Attempted to change to a sublocation from another sublocation!")
            return

        print(("Changing to sublocation {0}").format(sublocation))
        sublocation = location_manager[location].sublocations[sublocation]

        self.close_all_main_sections()

        if sublocation.type == LocationType.CLIENT:
            self.enable_section(CLIENT_SECTION) 
        elif sublocation.type == LocationType.SHOP:
            self.enable_section(SHOP_SECTION)
            self.game_sections[SHOP_SECTION].open(sublocation)
        elif sublocation.type == LocationType.HOME:
            self.enable_section(HOME_SECTION)

        self.change_main_section_state(MainSectionState.SUBLOCATION)

    def can_player_change_location(self, location):
        if (self.time.get_hour() + game_rules["LocationTravelTimeIncrement"]) >= game_rules["DayEndHour"] and location != "Home":
            return TravelStatus.DAY_OVER
        elif location == self.player.location:
            return TravelStatus.ALREADY_PRESENT
        else:
            return TravelStatus.FINE

    def can_player_change_sublocation(self, sublocation):
        if (self.time.get_hour() + game_rules["SublocationTravelTimeIncrement"]) >= game_rules["DayEndHour"] and sublocation != "Home":
            return TravelStatus.DAY_OVER
        elif sublocation == self.player.sublocation:
            return TravelStatus.ALREADY_PRESENT
        else:
            return TravelStatus.FINE

    def change_player_location(self, location):
        if self.can_player_change_location(location):
            self.time.increment_time(game_rules["LocationTravelTimeIncrement"])
            self.player.location = location
            self.display_current_location()

    def change_player_sublocation(self, sublocation):
        if self.can_player_change_location(sublocation):
            self.player.sublocation = sublocation
            self.display_current_sublocation()

    def change_main_section_state(self, new_state):
        self.main_section_state = new_state

    def display_map(self):
        self.close_all_main_sections()
        self.enable_section(MAP_SECTION)
        self.change_main_section_state(MainSectionState.MAP)
        self.game_sections[MAP_SECTION].open()


    #*********************************************
    # Books
    #*********************************************

    def purchase_book(self, shop_name, book):
        if shop_manager[shop_name].stock.remove_book(book):
            self.player.stock.add_book(book)
            for _, section in self.get_active_sections():
                section.refresh()

    #*********************************************
    # Time
    #*********************************************

    def increment_day(self):
        self.time.increment_day()

        
