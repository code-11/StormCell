import pygame
from pygame import Rect

from core.scenario import Scenario
from gui.frame import Frame
import os

from . import game_frame, menu_frame
from .scbutton import SCButton
from .gui_utils import auto_text


class MapChoiceFrame(Frame):
    def __init__(self, window, frame_changer):
        super().__init__(window, frame_changer)
        self.start_btn = SCButton('start-btn', Rect(self.get_width() - 120, self.get_height() - 80, 100, 60),
                                  self.default_font, 'Start')
        self.start_btn.on_click = lambda: None

        self.back_btn = SCButton('back-btn', Rect(20, self.get_height() - 80, 100, 60), self.default_font, 'Back')
        self.back_btn.on_click = lambda: self.frame_changer(menu_frame.MenuFrame(self.window, self.frame_changer))

        self.selected_scenario = None
        self.clear_scenario_description = lambda: None
        self.clear_place_selector = lambda: None

    def extract_file_name(self, map_path):
        return map_path.split("\\")[-1].split('.')[0]

    def extract_name(self, map_file_name):
        return " ".join(map_file_name.split("_")[:-1]).title()

    def extract_num_players(self, map_file_name):
        splits = map_file_name.split("_")
        return int(splits[-1])

    # def make_on_map_click(self, map_file_name):
    #     def on_map_click():
    #         new_scenario = Scenario.load_scenario(map_file_name)
    #         new_frame = game_frame.GameFrame(self.window, self.frame_changer, new_scenario)
    #         self.frame_changer(new_frame)
    #
    #     return on_map_click

    def make_on_scenario_click(self, map_file_name):
        this = self

        def on_scenario_click():
            this.selected_scenario = Scenario.load_scenario(map_file_name)
            this.clear_scenario_description()
            this.clear_place_selector()
            this.start_btn.on_click = lambda: self.frame_changer(game_frame.GameFrame(self.window, self.frame_changer, this.selected_scenario))

        return on_scenario_click

    def draw_map_list(self):
        buttons = []
        i = 0
        auto_text('map-list-title', self.window, self.text_save_map, self.default_font, 'Map list', (200, 80))
        for map_path in self.find_maps():
            map_file_name = self.extract_file_name(map_path)
            map_name = self.extract_name(map_file_name)

            btn = SCButton(map_file_name, Rect(100, (i * 60) + 100, 150, 35), self.default_font, map_name)

            btn.on_click = self.make_on_scenario_click(map_file_name=map_file_name)

            btn.draw_button(self.window, self.text_save_map)

            i += 1
            buttons.append(btn)
        return buttons

    def draw_map_config(self):
        third_x = self.window.get_width() / 3
        height = self.window.get_height()
        pygame.draw.line(self.window, 'white', (third_x, 0), (third_x, height))

        desc_rect = self.draw_map_description(third_x)
        this = self
        def inner_clear_description():
            pygame.draw.rect(this.window, 'black', desc_rect)
        self.clear_scenario_description = inner_clear_description

        y_end_of_thumb = self.draw_map_thumbnail()
        if self.selected_scenario is not None:
            place_rect=self.draw_place_selector(third_x, y_end_of_thumb)
            this = self
            def inner_clear_place_selector():
                pygame.draw.rect(this.window, 'black', place_rect)
            self.clear_place_selector = inner_clear_place_selector

    def draw_map_description(self, line_x):
        map_name = 'No Map Selected' if self.selected_scenario is None else self.selected_scenario.name
        header_x = line_x + 20
        header_y = 30
        name_w, name_h = auto_text('selected-map-name', self.window, self.text_save_map, self.default_font, map_name,
                                   (header_x, header_y))

        map_desc = '' if self.selected_scenario is None else self.selected_scenario.description
        y_max = 0
        x_max = 0
        for i, line in enumerate(map_desc.split('\n')):
            x_val = line_x + 20
            y_val = i * 15 + 60
            text_w, text_h = auto_text(f"selected-map-desc{i}", self.window, self.text_save_map, self.default_font, line.strip(),
                      (x_val, y_val))
            text_end_x = x_val + text_w
            text_end_y = y_val + text_h
            x_max = max(x_max, text_end_x)
            y_max = max(y_max, text_end_y)

        return Rect(header_x, header_y, x_max-header_x + 1, y_max-header_y + 1)

    def draw_map_thumbnail(self):
        width = self.window.get_width()
        left_side = width - 250 - 20
        right_side = width - 20
        thumb_width = right_side - left_side
        pygame.draw.rect(self.window, 'white', Rect(left_side, 20, thumb_width, thumb_width))

        # return y end of thumb
        return 20 + thumb_width

    def draw_place_selector(self, line_x, thumb_y):
        col_buffer = 100
        row_buffer = 40
        buffer_from_thumb = 30

        color_col = line_x + col_buffer
        col_w, col_h = auto_text('color-header', self.window, self.text_save_map, self.default_font, 'Nation',
                                 (color_col, thumb_y + buffer_from_thumb))

        type_col = color_col + col_w + col_buffer
        text_w, text_h = auto_text('type-header', self.window, self.text_save_map, self.default_font, 'Type', (type_col, thumb_y + buffer_from_thumb))
        max_text_w = text_w
        for i, nation in enumerate(self.selected_scenario.nations):
            loc_y = thumb_y + buffer_from_thumb + (1+i)*row_buffer
            text_w, text_h = auto_text(f"loc-{i}", self.window, self.text_save_map, self.default_font, nation.name,(color_col, loc_y))
            max_text_w = max(max_text_w, text_w)

        return Rect(color_col,thumb_y + buffer_from_thumb, max_text_w, text_h + loc_y)


    def find_maps(self):
        maps = []
        for file in os.listdir("./scenarios/maps/"):
            if file.endswith(".sc_map"):
                maps.append(os.path.join("/scenarios/maps", file))
        return maps

    def pre_event_draw(self):
        self.buttons = self.draw_map_list()
        self.more_buttons = self.draw_map_config()
        self.start_btn.draw_button(self.window, self.text_save_map)
        self.back_btn.draw_button(self.window, self.text_save_map)
        self.buttons.extend([self.start_btn, self.back_btn])

    def on_left_click(self, mouse):
        super().on_left_click(mouse)

    def on_right_click(self, mouse):
        pass

    def post_event_draw(self):
        pass
