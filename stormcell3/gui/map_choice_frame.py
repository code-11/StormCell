from pygame import Rect

from gui.frame import Frame
import os
from .scbutton import SCButton
from .gui_utils import auto_text


class MapChoiceFrame(Frame):
    def __init__(self, window, frame_changer):
        super().__init__(window, frame_changer)

    def extract_file_name(self, map_path):
        return map_path.split("\\")[-1].split('.')[0]

    def extract_name(self, map_file_name):
        return " ".join(map_file_name.split("_")[:-1]).title()

    def extract_num_players(self, map_file_name):
        splits = map_file_name.split("_")
        return int(splits[-1])

    def make_on_map_click(self, map_file_name):
        return lambda:print(map_file_name)

    def draw_map_list(self):
        buttons = []
        i = 0
        auto_text('map-list-title', self.window, self.text_save_map, self.default_font, 'Map list', (200, 80))
        for map_path in self.find_maps():
            map_file_name = self.extract_file_name(map_path)
            map_name = self.extract_name(map_file_name)

            btn = SCButton(map_file_name, Rect(200, (i * 60) + 100, 150, 35), self.default_font, map_name)

            btn.on_click = self.make_on_map_click(map_file_name=map_file_name)

            btn.draw_button(self.window, self.text_save_map)

            i += 1
            buttons.append(btn)
        return buttons

    def find_maps(self):
        maps = []
        for file in os.listdir("./scenarios/maps/"):
            if file.endswith(".sc_map"):
                maps.append(os.path.join("/scenarios/maps", file))
        return maps

    def pre_event_draw(self):
        self.buttons = self.draw_map_list()

    def on_left_click(self, mouse):
        super().on_left_click(mouse)

    def on_right_click(self, mouse):
        pass

    def post_event_draw(self):
        pass
