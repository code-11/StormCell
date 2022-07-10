import sys

import pygame
from pygame.rect import Rect

import gui.game_frame
from core.scenario import Scenario

from gui.frame import Frame
from gui.gui_utils import auto_text
from gui.scbutton import SCButton
from gui.map_choice_frame import MapChoiceFrame
# from scenarios.test_scenario import TestScenario as TheScenario
from scenarios.scenario_gen_scripts.x_marks_the_spot_4 import XMarksTheSpot4 as TheScenario
# from scenarios.whirlpool_3 import Whirlpool3 as TheScenario

class MenuFrame(Frame):

    def __init__(self, window, frame_changer):
        super().__init__(window, frame_changer)
        self.title_font = pygame.freetype.Font(
            "C:\\Users\\brend\\Documents\\StormCell\\stormCell3\\resources\\fonts\\vecna\\Vecna.otf",
            60)

    def change_frame_to_map_choice(self):
        new_frame = MapChoiceFrame(self.window, self.frame_changer)
        self.frame_changer(new_frame)

    def change_frame_to_game(self):
        scenario = TheScenario()
        scenario.set_all_undefeated()
        new_frame = gui.game_frame.GameFrame(self.window, self.frame_changer, scenario)
        self.frame_changer(new_frame)

    def change_frame_to_load_game(self):
        scenario = Scenario.load_scenario()
        new_frame = gui.game_frame.GameFrame(self.window, self.frame_changer, scenario)
        self.frame_changer(new_frame)


    def quit(self):
        pygame.quit()
        sys.exit()

    def pre_event_draw(self):
        auto_text('title',
                  self.window,
                  self.text_save_map,
                  self.title_font,
                  'STORMCELL',
                  (320,100),
                  text_color='white',
                  background_color='black')

        btn1 = SCButton('play-btn', Rect(400, 180, 150, 45), self.default_font, 'Play')
        btn1.on_click = self.change_frame_to_map_choice

        btn2 = SCButton('load-btn', Rect(400, 240, 150, 45), self.default_font, 'Load')
        btn2.on_click = self.change_frame_to_load_game

        btn3 = SCButton('how-to-play', Rect(400, 300, 150, 45), self.default_font, 'How to Play')
        btn3.on_click = lambda: None

        btn4 = SCButton('settings', Rect(400, 360, 150, 45), self.default_font, 'Settings')
        btn4.on_click = lambda: None

        btn5 = SCButton('credits', Rect(400, 420, 150, 45), self.default_font, 'Credits')
        btn5.on_click = lambda: None

        btn6 = SCButton('quit', Rect(400, 480, 150, 40), self.default_font, 'Quit')
        btn6.on_click = self.quit

        self.buttons = [btn1, btn2, btn3, btn4, btn5, btn6]
        for btn in self.buttons:
            btn.draw_button(self.window, self.text_save_map)


    def on_left_click(self, mouse):
        super().on_left_click(mouse)

    def on_right_click(self, mouse):
        pass

    def post_event_draw(self):
        pass