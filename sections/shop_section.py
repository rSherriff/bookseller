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
        
        button_x = shop_screen_info["books"]["x"] + shop_screen_info["books"]["button_delta"]
        self.ui.setup_book_buttons(button_x,shop_screen_info["books"]["y"],shop_screen_info["books"]["gap"],self.shop.name,self.shop.stock.get_book_ids())

    def update(self):
        super().update()
    
    def render(self, console):
        super().render(console)

        console.print_box(shop_screen_info["title"]["x"],shop_screen_info["title"]["y"],shop_screen_info["title"]["width"],shop_screen_info["title"]["height"], string=self.shop.name, fg=(255,255,255), alignment=tcod.CENTER)

        info_text = "The following books catch your eye:"
        console.print_box(shop_screen_info["shop_info"]["x"],shop_screen_info["shop_info"]["y"],len(info_text), height=1, string=info_text, fg=(255,255,255), alignment=tcod.CENTER)

        count = 0
        for book in self.shop.stock.values():
            console.print(shop_screen_info["books"]["x"],shop_screen_info["books"]["y"]+ (count * shop_screen_info["books"]["gap"]),"{0}: {1}".format(book.id, book.title), fg=(255,255,255))

            button_x = shop_screen_info["books"]["x"] + shop_screen_info["books"]["button_delta"]
            console.print(button_x,shop_screen_info["books"]["y"]+ (count * shop_screen_info["books"]["gap"]),"Buy")
            count += 1

        self.render_ui(console)
      
    def mousedown(self,button,x,y):
        pass

    def keydown(self, key):
        pass

    