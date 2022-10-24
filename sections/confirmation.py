from sections.section import Section
from actions.actions import Action
from ui.confirmation_ui import ConfirmationUI


class Confirmation(Section):
    def __init__(self, engine, x: int, y: int, width: int, height: int, name:str):
        super().__init__(engine, x, y, width, height, "confirmation_dialog.xp", name)

        self.text = ""
        self.ui = ConfirmationUI(self, x, y, self.tiles["graphic"])

    def setup(self, text, confirmation_action, section, enable_ui_on_confirm):
        self.text = text
        self.ui.reset(confirmation_action, section, enable_ui_on_confirm)

    def render(self, console):
        super().render(console)
        console.print(self.x + 4, self.y + 2, self.text, (255, 255, 255))
