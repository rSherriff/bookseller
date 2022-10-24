from enum import Enum, auto
import string
from threading import Timer
from tkinter.dialog import DIALOG_ICON

import tcod
from image import Image

from sections.section import Section


class CharacterStates(Enum):
    TALK_ONE = auto()
    TALK_TWO = auto()

client_character_info = {
    "x":2,
    "y":2,
    "width":11,
    "height":14,
    "sprites":{
        "talk_one":{
            "x":0,
            "y":0
        },
        "talk_two":{
            "x":12,
            "y":0
        }
    }
}

client_misc_tiles_info = {
    "speech_mark":
    {
        "x":0,
        "y":0,
        "width":3,
        "height":3
    }
}

client_screen_info = {
    "text":
    {
        "x":18,
        "y":4,
        "width":30,
        "height":10
    },
    "speech_mark":
    {
        "x":14,
        "y":4,
        "width":3,
        "height":3
    }
}

class ClientSectionState(Enum):
    IDLE = auto(),
    DIALOG = auto()

class ClientSection(Section):
    def __init__(self, engine, x: int, y: int, width: int, height: int, name: string):
        super().__init__(engine, x, y, width, height, "client_section.xp", name)   
        
        self.client_character_tiles = Image(self.width, self.height, "images/client_character.xp")
        self.client_misc_tiles = Image(self.width, self.height, "images/client_misc.xp")

        self.animation_tick_interval = 0.3
        self.animation_tick = 0
        
        self.text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
        self.dialog_tick_interval = 0.1
        self.character_currently_talking = False
        self.current_dialog_index = 0

        self.reset()
        
    def reset(self):
        self.state = ClientSectionState.IDLE
        self.current_dialog_index = 0
        self.animation_tick = 0

        self.dialog_tick_loop()
        self.animation_tick_loop()

    def update(self):
        super().update()
    
    def render(self, console):
        super().render(console)

        if self.state == ClientSectionState.IDLE:
            self.draw_character(console, "talk_one")
            console.print_box(20,6,25,5, string="Press 'spacebar' to hear the client's order", alignment=tcod.CENTER, fg = (255,255,255))
        elif self.state == ClientSectionState.DIALOG:

            if self.animation_tick % 2 == 0 or not self.character_currently_talking:
                self.draw_character(console, "talk_one")
            else:
                self.draw_character(console, "talk_two")
        
            #Draw Speech Mark
            speech_mark_console = tcod.Console(client_misc_tiles_info["speech_mark"]["width"], client_misc_tiles_info["speech_mark"]["height"], order="F")
            x = client_misc_tiles_info["speech_mark"]["x"]
            y = client_misc_tiles_info["speech_mark"]["y"]
            xw = x + client_misc_tiles_info["speech_mark"]["width"]
            yh = y + client_misc_tiles_info["speech_mark"]["height"]
            speech_mark_console.tiles_rgb[0:client_misc_tiles_info["speech_mark"]["width"],0:client_misc_tiles_info["speech_mark"]["height"]] = self.client_misc_tiles.tiles[x:xw,y:yh]["graphic"]
            speech_mark_console.blit(console, src_x=0, src_y=0, dest_x=client_screen_info["speech_mark"]["x"], dest_y=client_screen_info["speech_mark"]["y"], width=client_screen_info["speech_mark"]["width"], height=client_screen_info["speech_mark"]["height"], bg_alpha=0)
            
            if self.current_dialog_index > len(self.text):
                self.character_currently_talking = False
            self.current_dialog_index = min(len(self.text), self.current_dialog_index)
            console.print_box(client_screen_info["text"]["x"], client_screen_info["text"]["y"], client_screen_info["text"]["width"], client_screen_info["text"]["height"], string=self.text[0:self.current_dialog_index], alignment=tcod.LEFT, fg = (255,255,255))

    def close(self):
        self.reset()

    def mousedown(self,button,x,y):
        pass

    def keydown(self, key):
        if self.state == ClientSectionState.IDLE and key == tcod.event.K_SPACE:
            self.change_state(ClientSectionState.DIALOG)

    def change_state(self, new_state):
        self.state = new_state

        if new_state == ClientSectionState.DIALOG:
            self.character_currently_talking = True

    def draw_character(self, console, state):
        character_console = tcod.Console(width=client_character_info["width"], height=client_character_info["height"], order="F")

        x = client_character_info["sprites"][state]["x"]
        y = client_character_info["sprites"][state]["y"]
        xw = x + client_character_info["width"]
        yh = y + client_character_info["height"]
        character_console.tiles_rgb[0:client_character_info["width"],0:client_character_info["height"]] = self.client_character_tiles.tiles[x:xw,y:yh]["graphic"]

        character_console.blit(console, src_x=0, src_y=0, dest_x=client_character_info["x"], dest_y=client_character_info["y"], width=client_character_info["width"], height=client_character_info["height"], bg_alpha=0)

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

    