from ui.ui import UI, Button, Tooltip

from actions.actions import  CloseNotificationDialog


class NotificationUI(UI):
    def __init__(self, section, x, y, tiles, width, height):
        super().__init__(section, x, y)
        self.elements = list()

        half_width = int(width / 2)
        
        bd = [14, 0, 9, 5]
        button_x = half_width-int(bd[2]/2)
        button_y = height - bd[3] - 2
        button_tiles = tiles[bd[0]:bd[0] + bd[2], bd[1]:bd[1] + bd[3]]
        close_button = Button(x=button_x, y=button_y, width=bd[2], height=bd[3], click_action=CloseNotificationDialog(self.section.engine, None), tiles=button_tiles)
        self.add_element(close_button)

    def reset(self, confirmation_action):
        self.elements[0].set_action(confirmation_action)
