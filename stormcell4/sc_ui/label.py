import pygame

class Label(object):
    def __init__(self, txt, location, size=(160,30), bg=pygame.Color('white'), fg=pygame.Color('black'), font_name="Segoe Print", font_size=12):
        self.bg = bg
        self.fg = fg
        self.size = size

        self.font = pygame.font.Font(font_name, font_size)
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        self.txt_rect = self.txt_surf.get_rect(center=[s//2 for s in self.size])

        self.surface = pygame.surface.Surface(size)
        self.rect = self.surface.get_rect(topleft=location)


    def draw(self,screen):
        self.surface.fill(self.bg)
        self.surface.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surface, self.rect)


    def update(self):
        self.txt_surf = self.font.render(self.txt, 1, self.fg)

        self.surface.blit(self.txt_surf, self.txt_rect)