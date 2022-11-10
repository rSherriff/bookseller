import string

from locations import location_manager
from ui.museum_ui import MuseumUI
import tcod

from sections.section import Section
from sections.section_layouts import museum_screen_info


class MuseumSection(Section):
    def __init__(self, engine, x: int, y: int, width: int, height: int, name: str):
        super().__init__(engine, x, y, width, height, "museum_section.xp", name)     
        self.ui = MuseumUI(self,x,y,self.tiles["graphic"])
        self.sublocation = location_manager["Bloomsbury"].sublocations["Museum"]

    def open(self):
        self.refresh()

    def refresh(self):
        self.ui.clear()
        self.ui.setup_search_bar()

    def close(self):
        self.ui.clear()

    def update(self):
        super().update()
    
    def render(self, console):
        super().render(console)

        console.print_box(museum_screen_info["title"]["x"],museum_screen_info["title"]["y"],museum_screen_info["title"]["width"],museum_screen_info["title"]["height"], string=self.sublocation.name, fg=(255,255,255), alignment=tcod.CENTER)
        console.print_box(museum_screen_info["description"]["x"],museum_screen_info["description"]["y"],museum_screen_info["description"]["width"],museum_screen_info["description"]["height"], string=self.sublocation.desc, fg=(255,255,255), alignment=tcod.LEFT)

        self.render_ui(console)
      
    def mousedown(self,button,x,y):
        pass

    def keydown(self, key):
        pass

    