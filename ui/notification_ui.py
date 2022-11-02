from ui.ui import UI, Button, Tooltip

from actions.actions import  CloseNotificationDialog


class NotificationUI(UI):
    def __init__(self, section, x, y, b_x, b_y,b_width, b_height):
        super().__init__(section, x, y)

        close_button = Button(x=b_x, y=b_y, width=b_width, height=b_height, click_action=CloseNotificationDialog(self.section.engine, None))
        self.add_element(close_button)

    def reset(self, confirmation_action):
        self.elements[0].set_action(confirmation_action)
