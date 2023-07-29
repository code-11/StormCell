import pygame


class SideBar():
    def __init__(self, location, size):
        self.size=size
        self.surface = pygame.surface.Surface(size)
        self.rect = self.surface.get_rect(topleft=location)

    def draw(self, screen):
        self.surface.fill(pygame.Color('white'))
        # self.surface.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surface, self.rect)
