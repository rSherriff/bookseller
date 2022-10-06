import tcod

from sections.section import Section


class InfoSection(Section):
    def __init__(self, engine, x: int, y: int, width: int, height: int):
        super().__init__(engine, x, y, width, height, "info_section.xp")      

    def update(self):
        super().update()
    
    def render(self, console):
        super().render(console)

        temp_console = tcod.Console(width=self.width, height=self.height, order="F")
        temp_console.print(1,3, ("Day: {0}").format(self.engine.player.day))
        temp_console.print(1,4, ("Loc: {0}").format(self.engine.player.location))
        temp_console.blit(console, src_x=0, src_y=0, dest_x=self.x, dest_y=self.y, width=self.width, height=self.height, bg_alpha=0)

      
    def mousedown(self,button,x,y):
        pass

    def keydown(self, key):
        pass

    