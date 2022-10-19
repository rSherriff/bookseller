import tcod

from sections.section import Section


class InfoSection(Section):
    def __init__(self, engine, x: int, y: int, width: int, height: int):
        super().__init__(engine, x, y, width, height, "info_section.xp")      

    def update(self):
        super().update()
    
    def render(self, console):
        super().render(console)

        console.print(self.x+1,self.y+3, ("Day: {0}").format(self.engine.player.day))
        console.print(self.x+1,self.y+4, ("Loc: {0}").format(self.engine.player.location))
        console.print(self.x+1,self.y+5, "Inv:")

        count = 0
        for book in self.engine.player.stock.values():
            console.print(self.x+5,self.y+6+count, book.id)
            count += 1

      
    def mousedown(self,button,x,y):
        pass

    def keydown(self, key):
        pass

    