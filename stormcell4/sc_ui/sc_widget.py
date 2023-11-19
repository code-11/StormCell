from typing import Tuple, Optional

from pygame import Rect


class SCWidget(object):

    def __init__(self):
        self.parent = None
        self.prev_location: Optional[Tuple[float, float]] = None
        self.callback = lambda *args: None

    def get_width(self):
        return 0

    def get_height(self):
        return 0

    def get_size(self):
        return self.get_width(), self.get_height()

    def draw(self, screen, location):
        pass

    def update(self):
        pass

    def get_surface(self):
        pass

    def set_last_location(self, location):
        self.prev_location = location

    def set_on_click(self, callback=lambda *args: None):
        self.callback = callback

    def on_click_propagation(self, pos):
        pass

    def on_click(self, pos):
        should_refresh = False
        width = self.get_width()
        height = self.get_height()
        if width != 0 and height != 0:
            if self.prev_location:
                x, y = self.prev_location
                if Rect(x, y, width, height).collidepoint(pos):
                    # print(f"Clicked {self}, pos {pos}")
                    should_refresh = should_refresh or self.callback()
                    should_refresh = should_refresh or self.on_click_propagation((pos[0] - x, pos[1] - y))
        return should_refresh
