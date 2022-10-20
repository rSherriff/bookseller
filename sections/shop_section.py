from sections.section import Section
from shops import *
from ui.shop_ui import ShopUI


shop_screen_info = {
    "books":{
        "x":6,
        "y":7,
        "gap": 2,
        "button_delta" : 25
    }
}

class ShopSection(Section):
    def __init__(self, engine, x: int, y: int, width: int, height: int):
        super().__init__(engine, x, y, width, height, "shop_section.xp")

        self.name = "ShopSection"
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

        console.print(4,4,"We are at {0}".format(self.shop.name))

        console.print(4,6,"Stock:")
        count = 0
        for book in self.shop.stock.values():
            console.print(shop_screen_info["books"]["x"],shop_screen_info["books"]["y"]+ (count * shop_screen_info["books"]["gap"]),"{0}: {1}".format(book.id, book.title))

            button_x = shop_screen_info["books"]["x"] + shop_screen_info["books"]["button_delta"]
            console.print(button_x,shop_screen_info["books"]["y"]+ (count * shop_screen_info["books"]["gap"]),"Buy")
            count += 1

        #self.ui.render(console) We are not rendering the UI, this may cause issues! This makes the current buttons work!
      
    def mousedown(self,button,x,y):
        pass

    def keydown(self, key):
        pass

    