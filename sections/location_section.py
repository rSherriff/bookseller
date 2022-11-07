import string

from locations import location_manager
from ui.location_ui import LocationUI
import tcod

from sections.section import Section
from sections.section_layouts import location_screen_info


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
        self.ui.setup_search_bar(self.location.name)

    def close(self):
        self.ui.clear()

    def update(self):
        super().update()
    
    def render(self, console):
        super().render(console)

        console.print_box(location_screen_info["title"]["x"],location_screen_info["title"]["y"],location_screen_info["title"]["width"],location_screen_info["title"]["height"], string=self.location.name, fg=(255,255,255), alignment=tcod.CENTER)

        count = 0
        for location in self.location.sublocations.values():
            if not location.hidden:
                console.print(location_screen_info["locations"]["x"],location_screen_info["locations"]["y"]+ (count * location_screen_info["locations"]["gap"]),"{0}".format(location.name), fg=(255,255,255))

                button_x = location_screen_info["locations"]["x"] + location_screen_info["locations"]["button_delta"]
                console.print(button_x,location_screen_info["locations"]["y"]+ (count * location_screen_info["locations"]["gap"]),"Go")
            count += 1

        console.print_box(location_screen_info["description"]["x"],location_screen_info["description"]["y"],location_screen_info["description"]["width"],location_screen_info["description"]["height"], string=self.location.desc, fg=(255,255,255), alignment=tcod.LEFT)

        self.render_ui(console)
      
    def mousedown(self,button,x,y):
        pass

    def keydown(self, key):
        pass

    