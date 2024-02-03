import pygame

from sc_ui.sc_image import SCImage
from sc_ui.sc_widget import SCWidget


class SelectableImage(SCWidget):
    def __init__(self, image: SCImage, select_color, select_border_size=2, padding=1, selected=False):
        super().__init__()
        self._image = image
        self.select_color = select_color
        self.select_size = select_border_size
        self.padding = padding
        self.selected = selected

    def on_click_propagation(self, pos):
        return self._image.on_click(pos)

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def update(self, the_game):
        self._image.update(the_game)
        extra_size = self.padding + self.select_size
        self._height = self._image.get_height() + (extra_size * 2)
        self._width = self._image.get_width() + (extra_size * 2)
        self._surface = pygame.surface.Surface(self.get_size())
        self._surface.fill(self.select_color)
        # pygame.draw.rect(self._surface, (255,255,255), pygame.Rect(self.padding, self.padding, self._image.get_height()+self.padding, self.get_width()+self.padding))
        self._image.draw(self._surface, (extra_size, extra_size))


    def draw(self, surface, location):
        x_pos, y_pos = location
        surface.blit(self._surface, pygame.rect.Rect(x_pos, y_pos, self.get_width(), self.get_height()))


    @classmethod
    def using_name(cls,
                   image_name: str,
                   size=None,
                   border_size=0,
                   border_color=pygame.color.Color('black'),
                   selected_size=0,
                   select_color=pygame.color.Color('black'),
                   padding=0,
                   selected=False):
        if selected:
            the_image = SCImage.using_name(image_name, size, border_size, border_color)
            return SelectableImage(the_image, select_color, selected_size, padding, selected)
        else:
            return SCImage.using_name(image_name, size, border_size, border_color)