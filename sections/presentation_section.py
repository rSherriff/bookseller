import string
import tcod

from sections.section import Section
from actions.game_actions import PresentRequestSolutionAction


class PresentationSection(Section):
    def __init__(self, engine, x: int, y: int, width: int, height: int, name:str):
        super().__init__(engine, x, y, width, height, "presentation_section.xp",name)      

    def open(self, request_id, client_id):
        self.request_id = request_id
        self.client_id = client_id

    def update(self):
        super().update()
    
    def render(self, console):
        super().render(console)
        console.print(self.x+2,self.y+2,"Choose a book to present",fg=(255,255,255))
        count = 0
        if len(self.engine.player.stock.values()) > 0:
            for book in self.engine.player.stock.values():
                console.print(self.x+5,self.y+ 4 + (count * 2), book.title, fg=(255,255,255))
                count += 1
        else:
            console.print(self.x+5,self.y+ 4, "No books in inv.", fg=(255,255,255))
      
    def mousedown(self,button,x,y):
        pass

    def keydown(self, key):
        
        ##TEMP

        dc = 0
        if key >= tcod.event.K_1 and key <= tcod.event.K_9:
            dc = key - 48

        c = 0
        for book in self.engine.player.stock.values():
            if c == dc:
                PresentRequestSolutionAction(self.engine, self.request_id, book.id, self.client_id).perform()
                self.engine.close_presentation_dialog()
                return
            c += 1

    