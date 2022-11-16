import string

import tcod
from shops import *
from ui.shop_ui import ShopUI

from sections.section import Section
from sections.section_layouts import shop_screen_info


class ShopSection(Section):
    def __init__(self, engine, x: int, y: int, width: int, height: int, name: str):
        super().__init__(engine, x, y, width, height, "shop_section.xp", name)

        self.shop = None
        self.ui = ShopUI(self,x,y,self.tiles["graphic"])

    def open(self, shop_location):
        self.shop = shop_manager[shop_location.name]  
        self.refresh()

    def refresh(self):
        self.ui.clear()
        self.ui.setup_book_tooltips(shop_screen_info["books"]["x"],shop_screen_info["books"]["y"],shop_screen_info["books"]["gap"],self.shop.stock.get_book_ids())

        button_mask = [[False,False,False,False,False],[False,True,True,True,False],[False,False,False,False,False]]
        self.ui.setup_book_buttons(self.button_x()-1,shop_screen_info["books"]["y"]-1,shop_screen_info["books"]["gap"],self.shop.name,self.shop.stock.get_book_ids(),button_mask)

    def update(self):
        super().update()
    
    def render(self, console):
        super().render(console)

        console.print_box(shop_screen_info["title"]["x"],shop_screen_info["title"]["y"],shop_screen_info["title"]["width"],shop_screen_info["title"]["height"], string=self.shop.name, fg=(255,255,255), alignment=tcod.CENTER)

        if len(self.shop.stock.values()) > 0:
            info_text = "The following books catch your eye:"
        else:
            info_text = "No books here catch your eye."
            
        console.print_box(shop_screen_info["shop_info"]["x"],shop_screen_info["shop_info"]["y"],len(info_text), height=1, string=info_text, fg=(255,255,255), alignment=tcod.CENTER)

        count = 0
        for book in self.shop.stock.values():
            title = book.title + " " + ("." * (shop_screen_info["books"]["button_delta"] - len(book.title) - 1))
            console.print(shop_screen_info["books"]["x"],shop_screen_info["books"]["y"]+ (count * shop_screen_info["books"]["gap"]),title, fg=(255,255,255))

            console.draw_frame(self.button_x()-1,shop_screen_info["books"]["y"]+ (count * shop_screen_info["books"]["gap"])-1,width=shop_screen_info["button_width"],height=shop_screen_info["button_height"], decoration=shop_screen_info["button_decoration"], bg=shop_screen_info["b_bg_color"], fg=shop_screen_info["b_fg_color"])
            console.print_box(self.button_x(),shop_screen_info["books"]["y"]+ (count * shop_screen_info["books"]["gap"]),width=shop_screen_info["button_width"]-2,height=shop_screen_info["button_height"]-2,string="Buy",alignment=tcod.CENTER, bg=shop_screen_info["b_font_bg_color"], fg=shop_screen_info["b_font_fg_color"])
            count += 1

        self.render_ui(console)
      
    def mousedown(self,button,x,y):
        pass

    def keydown(self, key):
        pass

    def button_x(self):
        return  shop_screen_info["books"]["x"] + shop_screen_info["books"]["button_delta"]

    