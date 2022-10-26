from math import ceil

import tcod
from actions.actions import CloseNotificationDialog
from ui.notification_ui import NotificationUI

from sections.section import Section

button_width = 7

class Notification(Section):
    def __init__(self, engine, x: int, y: int, width: int, height: int, name:str):
        super().__init__(engine, x, y, width, height, "buttons.xp", name)

        self.text = ""
        
    def setup(self, text, section):
        self.text = text

        self.render_width = min(len(self.text), 25) 
        self.render_height = ceil(len(self.text) / self.render_width)
        self.render_width += 4
        self.render_height += 10
        
        self.render_width += self.width % 2

        self.render_width = max(self.render_width, (button_width * 2) + 7)

        self.x = int(self.width / 2) - int(self.render_width / 2)
        self.y = int(self.height / 2) - int(self.render_height / 2)
        self.render_x = self.x
        self.render_y = self.y

        close_action = CloseNotificationDialog(self.engine, section)

        self.ui = NotificationUI(self, self.x, self.y, self.tiles["graphic"], self.render_width, self.render_height)
        self.ui.reset(close_action)

    def render(self, console):
        console.draw_frame(x=self.render_x,y=self.render_y,width=self.render_width,height=self.render_height, decoration="╔═╗║ ║╚═╝", bg=(0,0,0), fg=(255,255,255))
        console.print_box(x=self.render_x+1,y=self.render_y+2,width=self.render_width-2,height=self.render_height-2,string=self.text,alignment=tcod.CENTER, bg=(0,0,0), fg=(255,255,255))

        if self.ui:
            self.ui.render(console) 
