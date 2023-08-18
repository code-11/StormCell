import pygame

from StormCell.stormcell4.sc_ui.sc_widget import SCWidget


class SCImage(SCWidget):
    def __init__(self, image_path, size=None, border_size=0, border_color=pygame.color.Color('black')):
        super().__init__()
        self.image_path=image_path
        img = pygame.image.load(image_path).convert_alpha()
        img = pygame.transform.scale(img, size)
        self._width=size[0]+2*border_size
        self._height=size[1]+2*border_size
        self._surface=pygame.surface.Surface(self.get_size())

        #This is static so we can just do update here
        pygame.draw.rect(self._surface,border_color,pygame.Rect(0,0,self.get_width(),self.get_height()))
        self._surface.blit(img, (border_size, border_size))

    def update(self):
        pass

    def draw(self, surface, location):
        surface.blit(self._surface, self._surface.get_rect(topleft=location))

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height


        # img = pygame.image.load("/Users/brendanritter/fun/StormCell/stormcell4/resources/images/spearhead.png").convert_alpha()
        # img = pygame.transform.scale(img, (52, 60))
        # # pygame.draw.rect(self.surface,'#E80755',pygame.Rect(0,0,62,70))
        # # self.surface.blit(img, (5, 5))