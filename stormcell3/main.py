import pygame, sys
from pygame.locals import *

from gui.game_frame import GameFrame
from Scenarios.test_scenario import TestScenario as TheScenario
# from Scenarios.x_marks_the_spot_4 import XMarksTheSpot4 as TheScenario
# from Scenarios.whirlpool_3 import Whirlpool3 as TheScenario
from gui.gui_utils import auto_text
from gui.menu_frame import MenuFrame

LEFT_BTN = 1
MIDDLE_BTN = 2
RIGHT_BTN = 3





def quit():
    pygame.quit()
    sys.exit()


def run():
    pygame.init()
    window = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption('StormCell3')

    scenario = TheScenario()
    scenario.set_all_undefeated()

    # font = pygame.freetype.Font("C:\\Users\\brend\\Documents\\StormCell\\stormCell3\\resources\\fonts\\vecna\\Vecna.otf", 12)
    # cur_frame = GameFrame(window, scenario)
    cur_frame = MenuFrame(window)

    while True:  # main game loop
        cur_frame.pre_event_draw()

        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()

            if event.type == MOUSEBUTTONDOWN and event.button == LEFT_BTN:
                cur_frame.on_left_click(mouse)

            if event.type == MOUSEBUTTONDOWN and event.button == RIGHT_BTN:
                cur_frame.on_right_click(mouse)

        cur_frame.post_event_draw()

        pygame.display.update()


if __name__ == '__main__':
    run()
