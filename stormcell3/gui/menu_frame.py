import pygame
from pygame.rect import Rect

from gui.frame import Frame
from gui.gui_utils import auto_text
from gui.scbutton import SCButton


class MenuFrame(Frame):

    def __init__(self, window):
        super().__init__(window)
        self.title_font = pygame.freetype.Font(
            "C:\\Users\\brend\\Documents\\StormCell\\stormCell3\\resources\\fonts\\vecna\\Vecna.otf",
            60)

    def pre_event_draw(self):
        auto_text('title',
                  self.window,
                  self.text_save_map,
                  self.title_font,
                  'STORMCELL',
                  (320,100),
                  text_color='white',
                  background_color='black')

        btn1 = SCButton('play-btn', Rect(400, 190, 150, 60), self.default_font, 'Play')
        btn1.on_click = lambda: None

        btn2 = SCButton('how-to-play', Rect(400, 290, 150, 60), self.default_font, 'How to Play')
        btn2.on_click = lambda: None

        btn3 = SCButton('settings', Rect(400, 390, 150, 60), self.default_font, 'Settings')
        btn3.on_click = lambda: None

        btn4 = SCButton('credits', Rect(400, 490, 150, 40), self.default_font, 'Credits')
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