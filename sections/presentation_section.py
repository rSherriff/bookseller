import string

import tcod

from actions.game_actions import PresentRequestSolutionAction
from sections.section import Section
from sections.section_layouts import presentation_dialog_info
from ui.presentation_ui import PresentationUI


class PresentationSection(Section):
    def __init__(self, engine, x: int, y: int, width: int, height: int, name:str):
        super().__init__(engine, x, y, width, height, "presentation_section.xp",name)  
        self.ui = PresentationUI(self,x,y,self.tiles["graphic"])    

    def open(self, request_id, client_id):
        self.request_id = request_id
        self.client_id = client_id
        self.refresh()

    def refresh(self):
        self.ui.setup_book_buttons(presentation_dialog_info["books"]["x"],presentation_dialog_info["books"]["y"]-1,presentation_dialog_info["books"]["gap"],self.request_id, self.client_id,self.engine.player.stock.get_book_ids() )

    def update(self):
        super().update()
    
    def render(self, console):
        super().render(console)
        console.print(self.x+2,self.y+2,"Choose a book:",fg=(255,255,255))
        count = 0
        if len(self.engine.player.stock.values()) > 0:
            for book in self.engine.player.stock.values():
                button_x = self.x + presentation_dialog_info["books"]["x"]
                button_y = self.y + presentation_dialog_info["books"]["y"]+ (count * presentation_dialog_info["books"]["gap"])
                button_width = len(book.title)
                button_height = presentation_dialog_info["button_height"]
                console.draw_frame(button_x,button_y-1,width=button_width+2,height=button_height, decoration=presentation_dialog_info["button_decoration"], bg=presentation_dialog_info["b_bg_color"], fg=presentation_dialog_info["b_fg_color"])
                console.print_box(button_x+1,button_y,width=button_width,height=button_height-2,string=book.title,alignment=tcod.CENTER, bg=presentation_dialog_info["b_font_bg_color"], fg=presentation_dialog_info["b_font_fg_color"])
                count += 1
        else:
            console.print(self.x+5,self.y+ 4, "No books in inv.", fg=(255,255,255))

        button_x = self.x + presentation_dialog_info["close_button"]["x"]
        button_y = self.y + presentation_dialog_info["close_button"]["y"]
        button_width = len(presentation_dialog_info["close_button"]["text"])
        button_height = presentation_dialog_info["button_height"]
        console.draw_frame(button_x,button_y,width=button_width+2,height=button_height, decoration=presentation_dialog_info["button_decoration"], bg=presentation_dialog_info["b_bg_color"], fg=presentation_dialog_info["b_fg_color"])
        console.print_box(button_x+1,button_y+1,width=button_width,height=button_height-2,string=presentation_dialog_info["close_button"]["text"],alignment=tcod.CENTER, bg=presentation_dialog_info["b_font_bg_color"], fg=presentation_dialog_info["b_font_fg_color"])

        self.render_ui(console)
      
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

    