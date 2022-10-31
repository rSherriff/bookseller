from utils.definitions import TravelStatus, AdvanceDayStatus

from actions.actions import Action


#*********************************************
# Locations
#*********************************************

class DisplayCurrentSublocationAction(Action):
    def perform(self) -> None:
        self.engine.display_current_sublocation()

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

class OpenChangePlayerLocationConfirmationAction(Action):
    def __init__(self, engine, text, location, confirmation_action,section, enable_ui_on_confirm) -> None:
        super().__init__(engine)
        self.text = text
        self.location = location
        self.section = section
        self.enable_ui_on_confirm = enable_ui_on_confirm
        self.confirmation_action = confirmation_action

    def perform(self) -> None:
        travelStatus = self.engine.can_player_change_location(self.location)
        if travelStatus == TravelStatus.FINE:
            return self.engine.open_confirmation_dialog(self.text, self.confirmation_action, self.section, self.enable_ui_on_confirm)
        elif travelStatus == TravelStatus.ALREADY_PRESENT:
            return self.engine.open_notification_dialog("You are already at this location!", self.section)
        elif travelStatus == TravelStatus.DAY_OVER:
            return self.engine.open_notification_dialog("It's getting late, you should return home.", self.section)


#*********************************************
# Books
#*********************************************

class PurchaseBook(Action):
    def __init__(self, engine, shop_name, book):
        super().__init__(engine)
        self.shop_name = shop_name
        self.book = book

    def perform(self):
        self.engine.purchase_book(self.shop_name, self.book)

#*********************************************
# Requests
#*********************************************

class PresentRequestSolutionAction(Action):
    def __init__(self, engine, request_id, solution_id, client_id):
        super().__init__(engine)
        self.request_id = request_id
        self.solution_id = solution_id
        self.client_id = client_id

    def perform(self):
        self.engine.present_request_solution(self.request_id, self.solution_id, self.client_id)


#*********************************************
# Time
#*********************************************

class AdvanceDayAction(Action):
    def perform(self) -> None:
        self.engine.advance_day()

class OpenAdvanceDayConfirmationAction(Action):
    def __init__(self, engine, text, confirmation_action,section, enable_ui_on_confirm) -> None:
        super().__init__(engine)
        self.text = text
        self.section = section
        self.enable_ui_on_confirm = enable_ui_on_confirm
        self.confirmation_action = confirmation_action

    def perform(self) -> None:
        advanceDayStatus = self.engine.can_advance_day()
        if advanceDayStatus == AdvanceDayStatus.FINE:
            return self.engine.open_confirmation_dialog(self.text, self.confirmation_action, self.section, self.enable_ui_on_confirm)
        elif advanceDayStatus == AdvanceDayStatus.TOO_EARLY:
            return self.engine.open_notification_dialog("It is too early to advance the day!", self.section)


