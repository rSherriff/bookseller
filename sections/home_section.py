from ui.map_ui import MapUI

from sections.section import Section


class HomeSection(Section):
    def __init__(self, engine, x: int, y: int, width: int, height: int):
        super().__init__(engine, x, y, width, height, "home_section.xp")      

    def update(self):
        super().update()
    
    def render(self, console):
        super().render(console)
      
    def mousedown(self,button,x,y):
        pass

    def keydown(self, key):
        pass

    