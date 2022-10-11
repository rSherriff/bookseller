from sections.section import Section

class ShopSection(Section):
    def __init__(self, engine, x: int, y: int, width: int, height: int):
        super().__init__(engine, x, y, width, height, "shop_section.xp")

        self.shop = None

    def setup(self, shop_location):
        self.shop = self.engine.shop_manager.shops[shop_location.name]      

    def update(self):
        super().update()
    
    def render(self, console):
        super().render(console)

        console.print(4,4,"We are at {0}".format(self.shop.name))

        console.print(4,6,"Stock:")
        count = 0
        for book in self.shop.stock.values():
            console.print(6, 7 + count,"{0}: {1}".format(count+1, book.title))
            count += 1
      
    def mousedown(self,button,x,y):
        pass

    def keydown(self, key):
        pass

    