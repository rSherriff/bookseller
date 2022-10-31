import string
from enum import Enum, auto
from http import client
from threading import Timer
from tkinter.dialog import DIALOG_ICON

import tcod
from clients import client_manager
from game_structure import client_status, requests
from image import Image

from sections.section import Section
from sections.section_layouts import (client_character_info,
                                      client_misc_tiles_info,
                                      client_screen_info)


class CharacterStates(Enum):
    TALK_ONE = auto()
    TALK_TWO = auto()

class ClientSectionState(Enum):
    INTRO_REQUEST_OUTSTANDING = auto(),
    INTRO_REQUEST_COMPLETE = auto()
    IDLE = auto(),
    DIALOG = auto(),
    PRESENTATION = auto()

class ClientSection(Section):
    def __init__(self, engine, x: int, y: int, width: int, height: int, name: string):
        super().__init__(engine, x, y, width, height, "client_section.xp", name)   

        self.client_id = None
        
        self.client_character_tiles = Image(self.width, self.height, "images/client_character.xp")
        self.client_misc_tiles = Image(self.width, self.height, "images/client_misc.xp")

        self.animation_tick_interval = 0.3
        self.animation_tick = 0
        
        self.text = ""
        self.dialog_tick_interval = 0.1
        self.character_currently_talking = False
        self.current_dialog_index = 0
        self.state_after_dialog = None
        
    def open(self, client_id):
        self.client = client_manager[client_id]

        if len(self.client.available_requests) > 0:
            self.request = requests[self.client.available_requests[0]]

        if not self.client.served_today:
            self.state = ClientSectionState.INTRO_REQUEST_OUTSTANDING
        else:
            self.state = ClientSectionState.INTRO_REQUEST_COMPLETE

        self.animation_tick = 0

        self.dialog_tick_loop()
        self.animation_tick_loop()

    def update(self):
        super().update()
    
    def render(self, console):
        super().render(console)

        if self.state == ClientSectionState.IDLE:
            self.draw_character(console, "talk_one")
            self.draw_text(console)
        elif self.state == ClientSectionState.INTRO_REQUEST_OUTSTANDING:
            self.draw_character(console, "talk_one")
            console.print_box(20,6,25,5, string="Press 'spacebar' to hear the client's order", alignment=tcod.CENTER, fg = (255,255,255))
        elif self.state == ClientSectionState.INTRO_REQUEST_COMPLETE:
            self.draw_character(console, "talk_one")
            console.print_box(20,6,25,5, string="You have completed this client's order for today!", alignment=tcod.CENTER, fg = (255,255,255))
        elif self.state == ClientSectionState.DIALOG:

            if self.animation_tick % 2 == 0 or not self.character_currently_talking:
                self.draw_character(console, "talk_one")
            else:
                self.draw_character(console, "talk_two")
        
            self.draw_speech_mark(console)           
            
            if self.current_dialog_index > len(self.text):
                self.character_currently_talking = False
                self.change_state(self.state_after_dialog)
            self.current_dialog_index = min(len(self.text), self.current_dialog_index)

            self.draw_text(console)

        elif self.state == ClientSectionState.PRESENTATION:
            self.draw_character(console, "talk_one")
            self.draw_speech_mark(console)
            self.draw_text(console)

    def close(self):
        pass

    def mousedown(self,button,x,y):
        pass

    def keydown(self, key):
        if self.state == ClientSectionState.INTRO_REQUEST_OUTSTANDING and key == tcod.event.K_SPACE and not self.client.served_today:
            self.start_character_talking(self.request["text"], ClientSectionState.PRESENTATION)
        elif self.state == ClientSectionState.DIALOG and key == tcod.event.K_SPACE:
            self.current_dialog_index = len(self.text)
        elif key == tcod.event.K_q and not self.client.served_today:
            self.start_character_talking(self.request["text"], ClientSectionState.PRESENTATION)
        elif key == tcod.event.K_e and not self.client.served_today:
            self.engine.open_presentation_dialog(self.request["id"], self.client.id)

    def change_state(self, new_state):
        self.state = new_state

        if new_state == ClientSectionState.DIALOG:
            self.character_currently_talking = True
        elif new_state == ClientSectionState.PRESENTATION:
            self.character_currently_talking = False

    def request_satisfied(self):
        self.start_character_talking("This is the correct book!", ClientSectionState.IDLE)
        self.request = None

    def request_failed(self):
        self.start_character_talking("This is the incorrect book!", ClientSectionState.IDLE)

    def start_character_talking(self, text, state_after_dialog):
        self.current_dialog_index = 0
        self.state_after_dialog = state_after_dialog
        self.text = text
        self.change_state(ClientSectionState.DIALOG)

    def draw_character(self, console, state):
        character_console = tcod.Console(width=client_character_info["width"], height=client_character_info["height"], order="F")

        x = client_character_info["sprites"][state]["x"]
        y = client_character_info["sprites"][state]["y"]
        xw = x + client_character_info["width"]
        yh = y + client_character_info["height"]
        character_console.tiles_rgb[0:client_character_info["width"],0:client_character_info["height"]] = self.client_character_tiles.tiles[x:xw,y:yh]["graphic"]

        character_console.blit(console, src_x=0, src_y=0, dest_x=client_character_info["x"], dest_y=client_character_info["y"], width=client_character_info["width"], height=client_character_info["height"], bg_alpha=0)

    def draw_speech_mark(self, console):
        speech_mark_console = tcod.Console(client_misc_tiles_info["speech_mark"]["width"], client_misc_tiles_info["speech_mark"]["height"], order="F")
        x = client_misc_tiles_info["speech_mark"]["x"]
        y = client_misc_tiles_info["speech_mark"]["y"]
        xw = x + client_misc_tiles_info["speech_mark"]["width"]
        yh = y + client_misc_tiles_info["speech_mark"]["height"]
        speech_mark_console.tiles_rgb[0:client_misc_tiles_info["speech_mark"]["width"],0:client_misc_tiles_info["speech_mark"]["height"]] = self.client_misc_tiles.tiles[x:xw,y:yh]["graphic"]
        speech_mark_console.blit(console, src_x=0, src_y=0, dest_x=client_screen_info["speech_mark"]["x"], dest_y=client_screen_info["speech_mark"]["y"], width=client_screen_info["speech_mark"]["width"], height=client_screen_info["speech_mark"]["height"], bg_alpha=0)

    def draw_text(self, console):
        console.print_box(client_screen_info["text"]["x"], client_screen_info["text"]["y"], client_screen_info["text"]["width"], client_screen_info["text"]["height"], string=self.text[0:self.current_dialog_index], alignment=tcod.LEFT, fg = (255,255,255))

    def animation_tick_loop(self):
        if not self.engine.is_section_disabled(self.name):
            self.animation_tick += 1
        t = Timer(self.animation_tick_interval, self.animation_tick_loop)
        t.daemon = True
        t.start()

    def dialog_tick_loop(self):
        if not self.engine.is_section_disabled(self.name) and self.state == ClientSectionState.DIALOG:
            self.current_dialog_index += 1
        t = Timer(self.dialog_tick_interval, self.dialog_tick_loop)
        t.daemon = True
        t.start()

    