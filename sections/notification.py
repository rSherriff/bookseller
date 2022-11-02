from math import ceil

import tcod
from actions.actions import CloseNotificationDialog
from ui.notification_ui import NotificationUI

from sections.section import Section
from sections.section_layouts import notification_dialog_info


class Notification(Section):
    def __init__(self, engine, x: int, y: int, width: int, height: int, name:str):
        super().__init__(engine, x, y, width, height, "buttons.xp", name)

        self.text = ""
        
    def setup(self, text, section):
        self.text = text

        self.render_width = min(len(self.text), notification_dialog_info["max_width"]) 
        self.render_height = ceil(len(self.text) / self.render_width)
        self.render_width += 4
        self.render_height += 10
        
        self.render_width += self.width % 2

        self.render_width = max(self.render_width, (notification_dialog_info["button_width"] * 2) + 7)

        self.x = int(self.width / 2) - int(self.render_width / 2)
        self.y = int(self.height / 2) - int(self.render_height / 2)
        self.render_x = self.x
        self.render_y = self.y

        close_action = CloseNotificationDialog(self.engine, section)

        self.ui = NotificationUI(self, self.x, self.y, self.button_x(), self.button_y(), notification_dialog_info["button_width"], notification_dialog_info["button_height"])
        self.ui.reset(close_action)

    def render(self, console):
        console.draw_frame(x=self.render_x,y=self.render_y,width=self.render_width,height=self.render_height, decoration="╔═╗║ ║╚═╝", bg=(0,0,0), fg=(255,255,255))
        console.print_box(x=self.render_x+1,y=self.render_y+2,width=self.render_width-2,height=self.render_height-2,string=self.text,alignment=tcod.CENTER, bg=(0,0,0), fg=(255,255,255))

        console.draw_frame(x=self.x+self.button_x(),y=self.y+self.button_y(),width=notification_dialog_info["button_width"],height=notification_dialog_info["button_height"], decoration="╔═╗║ ║╚═╝", bg=(0,0,0), fg=(255,255,255))
        console.print_box(x=self.x+self.button_x()+1,y=self.y+self.button_y()+2,width=notification_dialog_info["button_width"]-2,height=notification_dialog_info["button_height"]-2,string="Close",alignment=tcod.CENTER, bg=(0,0,0), fg=(255,255,255))

        self.render_ui(console) 

    def button_x(self):
        half_width = int(self.render_width / 2)
        return half_width-int(notification_dialog_info["button_width"]/2)

    def button_y(self):
        return self.render_height - notification_dialog_info["button_height"] - 2
