import string
from ui.location_ui import LocationUI

from sections.section import Section
from locations import location_manager

location_screen_info = {
    "locations":{
        "x":6,
        "y":7,
        "gap": 2,
        "button_delta" : 25
    }
}

class LocationSection(Section):
    def __init__(self, engine, x: int, y: int, width: int, height: int, name: str):
        super().__init__(engine, x, y, width, height, "location_section.xp", name)     
        self.ui = LocationUI(self,x,y,self.tiles["graphic"])

    def open(self, location_name):
        self.location = location_manager[location_name]
        self.refresh()

    def refresh(self):
        self.ui.clear()
       
        button_x = location_screen_info["locations"]["x"] + location_screen_info["locations"]["button_delta"]
        self.ui.setup_sublocation_buttons(button_x,location_screen_info["locations"]["y"],location_screen_info["locations"]["gap"],self.location.sublocations.keys())

    def close(self):
        self.ui.clear()

    def update(self):
        super().update()
    
    def render(self, console):
        super().render(console)
        console.print(1,1,self.location.name,fg=(255,255,255))

        count = 0
        for location in self.location.sublocations.values():
            console.print(location_screen_info["locations"]["x"],location_screen_info["locations"]["y"]+ (count * location_screen_info["locations"]["gap"]),"{0}".format(location.name))

            button_x = location_screen_info["locations"]["x"] + location_screen_info["locations"]["button_delta"]
            console.print(button_x,location_screen_info["locations"]["y"]+ (count * location_screen_info["locations"]["gap"]),"Go")
            count += 1

        #self.ui.render(console) We are not rendering the UI, this may cause issues! This makes the current buttons work!
      
    def mousedown(self,button,x,y):
        pass

    def keydown(self, key):
        pass

    