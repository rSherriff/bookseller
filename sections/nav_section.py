from ui.nav_ui import NavUI

from sections.section import Section


class NavSection(Section):
    def __init__(self, engine, x: int, y: int, width: int, height: int):
        super().__init__(engine, x, y, width, height, "nav_section.xp")   

        self.ui = NavUI(self,x,y,self.tiles["graphic"])

    def update(self):
        super().update()
    
    def render(self, console):
        super().render(console)
      
    def mousedown(self,button,x,y):
        pass

    def keydown(self, key):
        pass
