import pygame
from pygame.font import get_default_font

from .sc_widget import SCWidget


class Label(SCWidget):
    def __init__(self, txt, location=None, bg=pygame.Color('white'), fg=pygame.Color('black'), font_name=get_default_font(),
                 font_size=12):
        super().__init__()
        self.bg = bg
        self.fg = fg

        self.font = pygame.font.Font(font_name, font_size)
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        this_size = self.txt_surf.get_size()
        self.txt_rect = self.txt_surf.get_rect(center=[s//2 for s in this_size])

        self.surface = pygame.surface.Surface(this_size)
        self.location=location

    def get_width(self):
        return self.txt_rect.width

    def get_height(self):
        return self.txt_rect.height

    def get_surface(self):
        return self.surface

    def draw(self,screen, location):
        self.surface.fill(self.bg)
        self.surface.blit(self.txt_surf, self.txt_rect)
        location_to_use=self.location if self.location else location
        screen.blit(self.surface, self.surface.get_rect(topleft=location_to_use))


    def update(self):
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        this_size = self.txt_surf.get_size()
        self.txt_rect = self.txt_surf.get_rect(center=[s//2 for s in this_size])

        self.surface = pygame.surface.Surface(this_size)
        self.surface.blit(self.txt_surf, self.txt_rect)