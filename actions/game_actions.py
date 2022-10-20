from actions.actions import Action

class DisplayCurrentLocationAction(Action):
    def perform(self) -> None:
        self.engine.display_current_location()

class DisplayMapAction(Action):
    def perform(self) -> None:
        self.engine.display_map()

class ChangePlayerLocationAction(Action):
    def __init__(self, engine, location) -> None:
        super().__init__(engine)
        self.location = location

    def perform(self):
        self.engine.change_player_location(self.location)

class ChangePlayerSublocationAction(Action):
    def __init__(self, engine, location) -> None:
        super().__init__(engine)
        self.location = location

    def perform(self):
        self.engine.change_player_sublocation(self.location)

class PurchaseBook(Action):
    def __init__(self, engine, shop_name, book):
        super().__init__(engine)
        self.shop_name = shop_name
        self.book = book

    def perform(self):
        self.engine.purchase_book(self.shop_name, self.book)
