from ui.ui import UI, Button, Tooltip

from actions.actions import CloseConfirmationDialog


class ConfirmationUI(UI):
    def __init__(self, section, x, y, tiles, width, height):
        super().__init__(section, x, y)
        self.elements = list()

        half_width = int(width / 2)
        
        bd = [0, 0, 7, 5]  # Button Dimensions
        button_x = half_width-bd[2]-1
        button_y = height - bd[3] - 2
        button_tiles = tiles[bd[0]:bd[0] + bd[2], bd[1]:bd[1] + bd[3]]
        self.confirm_button = Button(x=button_x, y=button_y, width=bd[2],height=bd[3], click_action=None, tiles=button_tiles, normal_bg=(0,0,0), highlight_bg=(255,255,255))
        self.add_element(self.confirm_button)

        self.confirm_close_button = Button(x=button_x, y=button_y, width=bd[2], height=bd[3], click_action=CloseConfirmationDialog(self.section.engine, None), tiles=button_tiles)
        self.add_element(self.confirm_close_button)

        bd = [7, 0, 7, 5]
        button_x = half_width +1 + (width % 2)
        button_tiles = tiles[bd[0]:bd[0] + bd[2], bd[1]:bd[1] + bd[3]]
        self.close_button = Button(x=button_x, y=button_y, width=bd[2], height=bd[3], click_action=CloseConfirmationDialog(self.section.engine, None), tiles=button_tiles)
        self.add_element(self.close_button)

    def reset(self, confirmation_action, section, enable_ui_on_confirm):
        self.confirm_button.set_action(confirmation_action)

        close_action=CloseConfirmationDialog(self.section.engine, section, enable_ui_on_confirm)
        self.confirm_close_button.set_action(close_action)

        close_action=CloseConfirmationDialog(self.section.engine, section, True) #Always enable UI on negative
        self.close_button.set_action(close_action)
