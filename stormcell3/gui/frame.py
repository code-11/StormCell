import sys

import pygame


class Frame(object):
    def __init__(self, window):
        self.window = window
        self.text_save_map = {}
        self.default_font = pygame.freetype.SysFont('Verdana', 12)
        self.buttons=[]

    def exit_to_menu():
        pygame.quit()
        sys.exit()

    def pre_event_draw(self):
        pass

    def on_left_click(self, mouse):
        for btn in self.buttons:
            btn.click_test(mouse)

    def on_right_click(self, mouse):
        pass

    def post_event_draw(self):
        pass