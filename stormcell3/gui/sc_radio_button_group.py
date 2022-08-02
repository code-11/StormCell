import pygame
from pygame import Rect

from gui.gui_utils import auto_text_extents
from gui.scbutton import SCButton


class SCRadioButtonGroup(object):
    def __init__(self, text_id_root, btn_texts, start_x, y, selected_index, font, click_callback, text_color='white', background_color='black'):
        super().__init__()
        self.font = font
        self.text_id_root = text_id_root
        self.text_color = text_color
        self.background_color = background_color
        self.y = y
        self.btn_texts = btn_texts
        self.selected_index = selected_index

        extents = [auto_text_extents(font, btn_text) for btn_text in btn_texts]
        height_max = max(map(lambda wh: wh[1], extents))

        x = start_x
        width = 0
        self.buttons = []

        for i, btn_text in enumerate(btn_texts):
            x += width + (0 if i == 0 else 6)
            width, height = extents[i]
            width += 6
            btn = SCButton(
                text_id_root + str(i),
                Rect(x, y, width, height_max + 6),
                font,
                btn_text,
                text_color,
                background_color)

            btn.on_click = lambda j=i: click_callback(j)
            self.buttons.append(btn)

    def draw_buttons(self, window, text_save_map):
        for i, btn in enumerate(self.buttons):
            should_frame = self.selected_index != i
            btn.draw_button(window, text_save_map, should_frame)
            if i == self.selected_index:
                pygame.draw.rect(window, 'darkgreen', btn.rect.inflate(2, 2), width=2)
