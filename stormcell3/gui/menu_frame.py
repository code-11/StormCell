from pygame.rect import Rect

from gui.frame import Frame
from gui.scbutton import SCButton


class MenuFrame(Frame):

    def __init__(self, window):
        super().__init__(window)

    def pre_event_draw(self):
        btn1 = SCButton('play-btn', Rect(300, 120, 150, 60), self.default_font, 'Play')
        btn1.on_click = lambda: None

        btn2 = SCButton('how-to-play', Rect(300, 220, 150, 60), self.default_font, 'How to Play')
        btn2.on_click = lambda: None

        btn3 = SCButton('settings', Rect(300, 320, 150, 60), self.default_font, 'Settings')
        btn3.on_click = lambda: None

        btn4 = SCButton('credits', Rect(300, 420, 150, 40), self.default_font, 'Credits')
        btn4.on_click = lambda: None

        self.buttons = [btn1, btn2, btn3, btn4]
        for btn in self.buttons:
            btn.draw_button(self.window, self.text_save_map)


    def on_left_click(self, mouse):
        super().on_left_click(mouse)

    def on_right_click(self, mouse):
        pass

    def post_event_draw(self):
        pass