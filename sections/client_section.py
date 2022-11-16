import string
from enum import Enum, auto
from http import client
from threading import Timer
from tkinter.dialog import DIALOG_ICON
from math import ceil

import tcod
from clients import client_manager
from game_structure import client_status, requests
from image import Image

from sections.section import Section
from sections.section_layouts import (client_character_info,
                                      client_misc_tiles_info,
                                      client_screen_info)
from utils.definitions import TextEffects


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

        # Request
        self.request = None
        
        # Dialog 
        self.text = ""
        self.dialog_tick_interval = 0
        self.character_currently_talking = False
        self.current_dialog_index = 0
        self.current_pause = 0
        self.text_effects = []
        self.state_after_dialog = None
        self.num_line_breaks = 0
        
    def open(self, client_id):
        self.client = client_manager[client_id]

        if not self.client.served_today:
            self.state = ClientSectionState.INTRO_REQUEST_OUTSTANDING
        else:
            self.state = ClientSectionState.INTRO_REQUEST_COMPLETE

        self.animation_tick = 0


    def update(self):
        super().update()

        if self.state == ClientSectionState.DIALOG:
            self.dialog_tick_loop()
                
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

            if self.get_animation_tick() % 2 == 0 or not self.character_currently_talking:
                self.draw_character(console, "talk_one")
            else:
                self.draw_character(console, "talk_two")
        
            self.draw_speech_mark(console)  

            if self.current_dialog_index > len(self.text):
                self.end_talking()
            self.current_dialog_index = min(len(self.text), self.current_dialog_index)

            self.draw_dialog(console)

        elif self.state == ClientSectionState.PRESENTATION:
            self.draw_character(console, "talk_one")
            self.draw_speech_mark(console)
            self.draw_dialog(console)

    def close(self):
        pass

    def mousedown(self,button,x,y):
        pass

    def keydown(self, key):
        if self.state == ClientSectionState.INTRO_REQUEST_OUTSTANDING and key == tcod.event.K_SPACE and not self.client.served_today:
            if self.start_request():
                self.start_character_talking(self.request["text"], ClientSectionState.PRESENTATION)
        elif self.state == ClientSectionState.DIALOG and key == tcod.event.K_SPACE:
            self.current_dialog_index = len(self.text) + (self.text.count('\n') * client_screen_info["text"]["max_width"])
            self.end_talking()
        elif key == tcod.event.K_q and not self.client.served_today:
            self.start_character_talking(self.request["text"], ClientSectionState.PRESENTATION)
        elif key == tcod.event.K_e and not self.client.served_today:
            if self.request != None:
                self.engine.open_presentation_dialog(self.request["id"], self.client.id)

    def change_state(self, new_state):
        self.state = new_state

        if new_state == ClientSectionState.DIALOG:
            self.character_currently_talking = True
            self.analyse_text()
            
        elif new_state == ClientSectionState.PRESENTATION:
            self.character_currently_talking = False

    def start_request(self):
        if len(self.client.available_requests) > 0:
            self.request = requests[self.client.available_requests[0]]
            self.engine.start_request(self.request["id"])
            return True
        return False

    def request_satisfied(self):
        self.start_character_talking("This is the correct book!", ClientSectionState.IDLE)
        self.request = None

    def request_failed(self):
        self.start_character_talking("This is the incorrect book!", ClientSectionState.IDLE)

    def start_character_talking(self, text, state_after_dialog):
        self.state_after_dialog = state_after_dialog
        self.reset_talking(text)
        self.change_state(ClientSectionState.DIALOG)

    def reset_talking(self, text):
        self.current_dialog_index = 1
        self.text = text

    def end_talking(self):
        self.character_currently_talking = False
        self.change_state(self.state_after_dialog)

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
        console.print_box(client_screen_info["text"]["x"], client_screen_info["text"]["y"], client_screen_info["text"]["width"], client_screen_info["text"]["height"], string=self.text[0:self.get_current_dialog_index()], alignment=tcod.LEFT, fg = (255,255,255))

    def draw_dialog(self, console):
        render_width =  client_screen_info["text"]["max_width"]
        render_height = ceil((self.get_current_dialog_index() + (render_width * self.num_line_breaks)) / render_width)
        render_width += 4
        render_height += 4

        console.draw_frame(x=client_screen_info["text"]["x"], y=client_screen_info["text"]["y"],width=render_width,height=render_height, decoration=client_screen_info["text"]["decoration"], bg=(0,0,0), fg=(255,255,255))
        console.print_box(x=client_screen_info["text"]["x"]+2, y=client_screen_info["text"]["y"]+2,width=render_width-3,height=render_height-2,string=self.text[0:self.get_current_dialog_index()],alignment=tcod.LEFT, bg=(255,255,255), fg=(0,0,0))

    def animation_tick_loop(self):
        if not self.engine.is_section_disabled(self.name):
            self.animation_tick += 1
 
    def get_animation_tick(self):
        return (self.animation_tick)

    def dialog_tick_loop(self):
        self.current_pause += self.engine.get_delta_time()
        self.current_pause = min(self.current_pause, 0)
        if self.current_pause >= 0:
            diff =  self.engine.get_delta_time() * 30
            if len(self.text_effects) >0:
                if self.text_effects[0]["type"] == TextEffects.PAUSE:  
                    if self.current_dialog_index + diff >= self.text_effects[0]["index"]:  
                        self.current_pause -= self.text_effects[0]["length"]   
                        self.current_dialog_index  = self.text_effects[0]["index"]   
                        self.text_effects.pop(0)  
                    else:
                        self.current_dialog_index += diff  
            else:
                self.current_dialog_index += diff  

        self.num_line_breaks = self.text[:self.get_current_dialog_index()].count('\n')

    def get_current_dialog_index(self):
        return (int(self.current_dialog_index))

    def analyse_text(self):
        split_text = self.text.split('#')
        final_text = ""
        for t in split_text:
            if t.startswith("pause="):
                t = t[len("pause="):]
                self.text_effects.append({"type":TextEffects.PAUSE,"index":len(final_text), "length":float(t)})
            else:
                final_text += t

        self.text = final_text
    