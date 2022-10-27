import json
from collections import OrderedDict
from datetime import date, datetime, timedelta
from enum import Enum, auto
from threading import Timer

from pygame import mixer

from books import *
from books import Stock
from effects.horizontal_wipe_effect import (HorizontalWipeDirection,
                                            HorizontalWipeEffect)
from effects.melt_effect import MeltWipeEffect, MeltWipeEffectType
from engine import CONFIRMATION_DIALOG, NOTIFICATION_DIALOG, Engine, GameState
from locations import *
from game_structure import storySegments, StoryTriggerType
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
from utils.definitions import AdvanceDayStatus, TravelStatus, AdvanceStoryStatus, StorySegmentWaiting

game_rules = {
    "LocationTravelTimeIncrement" : 1,
    "SublocationTravelTimeIncrement": 0,
    "DayStartHour": 10,
    "DayEndHour" : 18,
    "DayAdvanceHour": 17
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
        self.story_segment = "start"
        self.requestsPerformed = []

class TimeState:
    def __init__(self) -> None:
        self.dt = datetime(1983,4,13,game_rules["DayStartHour"])

    def advance_day(self):
        self.dt += timedelta(days=1)
        self.dt = self.dt.replace(hour= game_rules["DayStartHour"])

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
        self.setup_effects()
        self.start_game()
        

    def start_game(self):
        self.try_advance_story_segment()
        self.close_all_main_sections()
        self.display_current_sublocation()
        self.refresh_open_sections()

    def create_new_save_data(self):
        pass

    def load_initial_data(self, data):
        pass

    def load_fonts(self):
        pass

    #*********************************************
    # Effects
    #*********************************************

    def setup_effects(self):
        super().setup_effects()
        self.advance_day_effect = MeltWipeEffect(self, 0, 0, self.screen_width, self.screen_height, MeltWipeEffectType.RANDOM, 20)
        self.change_location_effect = HorizontalWipeEffect(self, 0, 0, self.screen_width, self.screen_height)

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
        self.game_sections[NAV_SECTION] = NavSection(self, 0,self.screen_height - 5, self.screen_width, 5, NAV_SECTION)
        
        
        self.misc_sections = OrderedDict()
        self.misc_sections[NOTIFICATION_DIALOG] = Notification(self, 0,0, self.screen_width, self.screen_height, NOTIFICATION_DIALOG)
        self.misc_sections[CONFIRMATION_DIALOG] = Confirmation(self, 0,0, self.screen_width, self.screen_height, CONFIRMATION_DIALOG)

        self.completion_sections = OrderedDict()

        self.disabled_sections = [CONFIRMATION_DIALOG, NOTIFICATION_DIALOG, MAP_SECTION, SHOP_SECTION, CLIENT_SECTION, HOME_SECTION, LOCATION_SECTION]
        self.disabled_ui_sections = [CONFIRMATION_DIALOG, NOTIFICATION_DIALOG, MAP_SECTION, SHOP_SECTION, CLIENT_SECTION, HOME_SECTION, LOCATION_SECTION]

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

    def refresh_open_sections(self):
        for key, section in self.get_active_sections():
            section.refresh()


    #*********************************************
    # Locations
    #*********************************************

    def display_current_location(self):
        self.display_location(self.player.location)
    
    def display_current_sublocation(self):
        self.display_sublocation(self.player.location, self.player.sublocation)

    def display_location(self, location):
        self.close_all_main_sections()
        self.enable_section(LOCATION_SECTION)
        self.game_sections[LOCATION_SECTION].open(location)
        print(("Changing to location {0}").format(location))
        self.change_main_section_state(MainSectionState.LOCATION)

    def display_sublocation(self, location, sublocation):
        if self.main_section_state == MainSectionState.SUBLOCATION and not sublocation == self.player.sublocation:
            print("WARNING! - Attempted to change to a sublocation from another sublocation!")
            return

        print(("Changing to sublocation {0}").format(sublocation))
        sublocation = location_manager[location].sublocations[sublocation]

        self.close_all_main_sections()

        if sublocation.type == LocationType.CLIENT:
            self.enable_section(CLIENT_SECTION) 
            self.game_sections[CLIENT_SECTION].open()
        elif sublocation.type == LocationType.SHOP:
            self.enable_section(SHOP_SECTION)
            self.game_sections[SHOP_SECTION].open(sublocation)
        elif sublocation.type == LocationType.HOME:
            self.enable_section(HOME_SECTION)
            self.game_sections[HOME_SECTION].open()

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
            self.player.sublocation = "none"
            self.time.increment_time(game_rules["LocationTravelTimeIncrement"])
            self.player.location = location
            self.display_current_location()
            self.set_full_screen_effect(self.change_location_effect, [HorizontalWipeDirection.LEFT])
            self.start_full_screen_effect()
            self.refresh_open_sections()

    def change_player_sublocation(self, sublocation):
        if self.can_player_change_location(sublocation):
            self.player.sublocation = sublocation
            self.display_current_sublocation()
            self.refresh_open_sections()

    def change_main_section_state(self, new_state):
        self.main_section_state = new_state

    def display_map(self):
        self.close_all_main_sections()
        self.enable_section(MAP_SECTION)
        self.change_main_section_state(MainSectionState.MAP)
        self.game_sections[MAP_SECTION].open()

    def are_currently_at_sublocation(self):
        return self.player.sublocation != "none"


    #*********************************************
    # Books
    #*********************************************

    def purchase_book(self, shop_name, book):
        if shop_manager[shop_name].stock.remove_book(book):
            self.player.stock.add_book(book)
            self.refresh_open_sections()

    #*********************************************
    # Time
    #*********************************************

    def advance_day(self):
        self.set_full_screen_effect(self.advance_day_effect)
        self.start_full_screen_effect()
        self.time.advance_day()

    def can_advance_day(self):
        if self.time.get_hour() < game_rules["DayAdvanceHour"]:
            return AdvanceDayStatus.TOO_EARLY
        else:
            return AdvanceDayStatus.FINE

    #*********************************************
    # Story
    #*********************************************
    
    def try_advance_story_segment(self):
        if self.should_display_next_story_segment() == AdvanceStoryStatus.FINE:
            segment = storySegments[storySegments[self.player.story_segment]["nextSegment"]]
            self.player.story_segment = segment["title"]
            if segment["location"] == LocationType.HOME:
                self.story_segment_waiting = StorySegmentWaiting.HOME
            elif segment["location"] == LocationType.CLIENT:
                self.story_segment_waiting = StorySegmentWaiting.CLIENT
            elif segment["location"] == LocationType.HOME:
                self.story_segment_waiting = StorySegmentWaiting.SHOP
        else:
            self.story_segment_waiting = StorySegmentWaiting.NONE

    def should_display_next_story_segment(self):
        next_segment = storySegments[self.player.story_segment]["nextSegment"]
        if next_segment != None:
            if storySegments[next_segment]["trigger"] == StoryTriggerType.NONE:
                return AdvanceStoryStatus.FINE
            elif storySegments[next_segment]["trigger"] == StoryTriggerType.REQUEST_NEEDED:
                if storySegments[next_segment]["requestsNeeded"] == None:
                    print("WARNING! - A segment is set as StoryTriggerType.REQUEST_NEEDED but has no required requests.")
                    return AdvanceStoryStatus.REQUEST_NOT_COMPLETED

                if all(r in self.player.requestsPerformed for r in storySegments[next_segment]["requestsNeeded"]):
                    return AdvanceStoryStatus.FINE
                else:
                    return AdvanceStoryStatus.REQUEST_NOT_COMPLETED

    def get_current_story_segment(self):
        return storySegments[self.player.story_segment]

    def get_story_segment_waiting(self):
        return self.story_segment_waiting

    def clear_story_segment_waiting(self):
        self.story_segment_waiting = StorySegmentWaiting.NONE
        

        
