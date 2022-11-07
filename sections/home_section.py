import string

import tcod
from ui.home_ui import HomeUI
from utils.definitions import StorySegmentWaiting

from sections.section import Section
from sections.section_layouts import home_screen_info


class HomeSection(Section):
    def __init__(self, engine, x: int, y: int, width: int, height: int, name:str):
        super().__init__(engine, x, y, width, height, "home_section.xp", name)      
        self.ui = HomeUI(self,x,y,self.tiles["graphic"])

    def open(self):
        self.refresh()

    def refresh(self):
        if self.engine.get_story_segment_waiting() == StorySegmentWaiting.HOME:
            self.engine.show_current_story_segment()
            
    def update(self):
        super().update()
    
    def render(self, console):
        super().render(console)
        console.print_box(home_screen_info["title"]["x"],home_screen_info["title"]["y"],home_screen_info["title"]["width"],home_screen_info["title"]["height"], string="Home", fg=(255,255,255), alignment=tcod.CENTER)

        self.render_ui(console)
              
    def mousedown(self,button,x,y):
        pass

    def keydown(self, key):
        pass

    