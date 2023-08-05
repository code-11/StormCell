import pygame

from StormCell.stormcell4.sc_ui.label import Label


class SideBar():
    def __init__(self, location, size):
        self.size=size
        self.surface = pygame.surface.Surface(size)
        self.rect = self.surface.get_rect(topleft=location)

    def draw(self, screen, game):
        self.surface.fill(pygame.Color('white'))
        # self.surface.blit(self.txt_surf, self.txt_rect)
        img = pygame.image.load("/Users/brendanritter/fun/StormCell/stormcell4/resources/images/spearhead.png").convert_alpha()
        img = pygame.transform.scale(img, (52, 60))

        country_title_text=Label(game.playing_as_country.name,(70,35))
        country_title_text.update()
        country_title_text.draw(self.surface)

        pygame.draw.rect(self.surface,'#E80755',pygame.Rect(0,0,62,70))
        self.surface.blit(img, (5, 5))
        screen.blit(self.surface, self.rect)
