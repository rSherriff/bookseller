

from actions.actions import OpenConfirmationDialog
from actions.game_actions import PresentRequestSolutionAction, ClosePresentationDialogAction

from ui.ui import UI, Tooltip, Button, Input
from books import book_manager
from sections.section_layouts import presentation_dialog_info


class PresentationUI(UI):
    def __init__(self, section,  x, y, tiles):
        super().__init__(section, x, y)
        self.tiles = tiles

        bd = [presentation_dialog_info["close_button"]["x"],presentation_dialog_info["close_button"]["y"],len(presentation_dialog_info["close_button"]["text"])+2, presentation_dialog_info["button_height"]]  # Button Dimensions
        b = Button(x=bd[0], y=bd[1], width=bd[2], height=bd[3], click_action=ClosePresentationDialogAction(self.section.engine),h_fg=presentation_dialog_info["b_h_color"])
        tl = [True]
        fl = [False]
        button_mask = [fl*bd[2], fl + (tl * (bd[2] - 2)) + fl,fl*bd[2]]
        b.set_mask(button_mask)
        self.add_element(b)

    def setup_book_buttons(self, x, y, y_gap, request_id, client_id, book_ids):
        count = 0
        for book_id in book_ids:
            book_title = book_manager[book_id].title
            bd = [x, y + ( y_gap * count),len(book_title)+2, presentation_dialog_info["button_height"]]  # Button Dimensions
            b = Button(x=bd[0], y=bd[1], width=bd[2], height=bd[3], click_action=OpenConfirmationDialog(
            self.section.engine, "Present {0}?".format(book_title), PresentRequestSolutionAction(self.section.engine, request_id, book_id, client_id), self.section.name, enable_ui_on_confirm=False),h_fg=presentation_dialog_info["b_h_color"])
            tl = [True]
            fl = [False]
            button_mask = [fl*bd[2], fl + (tl * (bd[2] - 2)) + fl,fl*bd[2]]
            b.set_mask(button_mask)
            self.add_element(b)
            count += 1