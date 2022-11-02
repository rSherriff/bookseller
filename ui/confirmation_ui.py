from ui.ui import UI, Button, Tooltip

from actions.actions import CloseConfirmationDialog


class ConfirmationUI(UI):
    def __init__(self, section, x, y, b_px, b_nx,  b_y,b_width, b_height):
        super().__init__(section, x, y)
        self.elements = list()

            
        bd = [0, 0, 7, 5]  # Button Dimensions

        
        self.confirm_button = Button(x=b_px, y=b_y, width=b_width,height=b_height, click_action=None)
        self.add_element(self.confirm_button)

        self.confirm_close_button = Button(x=b_px, y=b_y, width=b_width, height=b_height, click_action=CloseConfirmationDialog(self.section.engine, None))
        self.add_element(self.confirm_close_button)

        bd = [7, 0, 7, 5]

        self.close_button = Button(x=b_nx, y=b_y, width=b_width, height=b_height, click_action=CloseConfirmationDialog(self.section.engine, None))
        self.add_element(self.close_button)

    def reset(self, confirmation_action, section, enable_ui_on_confirm):
        self.confirm_button.set_action(confirmation_action)

        close_action=CloseConfirmationDialog(self.section.engine, section, enable_ui_on_confirm)
        self.confirm_close_button.set_action(close_action)

        close_action=CloseConfirmationDialog(self.section.engine, section, True) #Always enable UI on negative
        self.close_button.set_action(close_action)
