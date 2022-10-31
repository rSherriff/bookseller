import string
from ui.nav_ui import NavUI

from sections.section import Section

nav_section_info = {
    "date":
    {
        "x":30,
        "y":1
    },
    "time":
    {
        "x":30,
        "y":2
    },
    "location":
    {
        "x": 36,
        "y":2
    }
}

class NavSection(Section):
    def __init__(self, engine, x: int, y: int, width: int, height: int, name:str):
        super().__init__(engine, x, y, width, height, "nav_section.xp",name)   

        self.ui = NavUI(self,x,y,self.tiles["graphic"])
        
    def open(self):
        pass

    def refresh(self):
        self.ui.setup_nav_buttons()

    def update(self):
        super().update()
    
    def render(self, console):
        super().render(console)
        console.print(self.x+nav_section_info["date"]["x"],self.y+nav_section_info["date"]["y"], self.engine.time.get_date_string(), fg=(255,255,255))
        console.print(self.x+nav_section_info["time"]["x"],self.y+nav_section_info["time"]["y"], self.engine.time.get_hour_string(), fg=(255,255,255))
        console.print(self.x+nav_section_info["location"]["x"],self.y+nav_section_info["location"]["y"], self.engine.player.location, fg=(255,255,255))

        self.ui.render(console)
       
      
    def mousedown(self,button,x,y):
        pass

    def keydown(self, key):
        pass
