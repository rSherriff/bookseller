import string
from ui.map_ui import MapUI

from sections.section import Section

map_screen_info = {
    "locations":{
        ("Client", 12, 24, 7, 1),
        ("Bloomsbury", 28, 10, 11, 1)
    }
}

class MapSection(Section):
    def __init__(self, engine, x: int, y: int, width: int, height: int, name: str):
        super().__init__(engine, x, y, width, height, "map_section.xp", name)      

        self.ui = MapUI(self,x,y,self.tiles["graphic"])

    def open(self):
        self.refresh()

    def refresh(self):
        self.ui.setup_location_buttons(map_screen_info["locations"])

    def close(self):
        pass

    def update(self):
        super().update()

    def render(self, console):
        super().render(console)

        for location in map_screen_info["locations"]:
            console.print(location[1], location[2], "-"+location[0])
    
      
    def mousedown(self,button,x,y):
        pass

    def keydown(self, key):
        pass

    