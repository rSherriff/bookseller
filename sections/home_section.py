import string

import tcod
from actions.actions import OpenNotificationDialog
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
            segment = self.engine.get_current_story_segment()

            OpenNotificationDialog(self.engine, segment["text"], self).perform()
            self.engine.clear_story_segment_waiting()
            

    def update(self):
        super().update()
    
    def render(self, console):
        super().render(console)
              
    def mousedown(self,button,x,y):
        pass

    def keydown(self, key):
        pass

    