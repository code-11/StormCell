import pygame

from .gui_utils import auto_text


class SCButton(object):

    def __init__(self, text_id, rect, font, text, text_color='white', background_color='black'):
        super().__init__()
        self.rect = rect
        self.text = text
        self.font = font
        self.text_id = text_id
        self.text_color = text_color
        self.background_color = background_color

    def undraw_button(self, window, background_override=None):
        background_color_to_use = background_override if background_override is not None else self.background_color
        pygame.draw.rect(window, background_color_to_use, self.rect)

    def draw_button(self, window, text_save_map):
        x_pos = self.rect.midleft[0]+3
        y_pos = self.rect.topleft[1]+3

        self.undraw_button(window)

        for line in self.text.split('\n'):
            auto_text(self.text_id, window, text_save_map, self.font, line, (x_pos, y_pos),
                      text_color=self.text_color, background_color=self.background_color)
            y_pos += 15

        # text_width = 35
        # # text_width, text_height = pygame.font.Font.size(self.font,self.text)
        # text_pos_x = self.rect.centerx - text_width
        # self.font.render_to(window, (text_pos_x, self.rect.centery), self.text, 'white')
        pygame.draw.rect(window, 'white', self.rect, width=1)

    def click_test(self, mouse):
        if self.rect.collidepoint(mouse):
            self.on_click()

    def on_click(self):
        print('test')