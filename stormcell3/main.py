import pygame
import sys
from pygame.locals import *

from gui.menu_frame import MenuFrame

LEFT_BTN = 1
MIDDLE_BTN = 2
RIGHT_BTN = 3


class GameRunner(object):

    def __init__(self):
        super().__init__()
        self.frame = None

    def quit(self):
        pygame.quit()
        sys.exit()

    def run(self):
        pygame.init()
        window = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption('StormCell3')

        def change_frame(frame):
            window.fill('black')
            self.frame = frame

        self.frame = MenuFrame(window, change_frame)

        while True:  # main game loop
            self.frame.pre_event_draw()

            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == QUIT:
                    quit()

                if event.type == MOUSEBUTTONDOWN and event.button == LEFT_BTN:
                    self.frame.on_left_click(mouse)

                if event.type == MOUSEBUTTONDOWN and event.button == RIGHT_BTN:
                    self.frame.on_right_click(mouse)

            self.frame.post_event_draw()

            pygame.display.update()


if __name__ == '__main__':
    main = GameRunner()
    main.run()
