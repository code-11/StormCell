import pygame

class SCButton(object):
    def __init__(self, rect, font, text):
        super().__init__()
        self.rect = rect
        self.text = text
        self.font = font

    def draw_button(self, window):
        text_width = 35
        # text_width, text_height = pygame.font.Font.size(self.font,self.text)
        text_pos_x = self.rect.centerx - text_width
        self.font.render_to(window, (text_pos_x, self.rect.centery), self.text, 'white')
        pygame.draw.rect(window, 'white', self.rect, width=1)

    def click_test(self, mouse):
        if self.rect.collidepoint(mouse):
            self.on_click()

    def on_click(self):
        print('test')