from enum import Enum
from typing import List

import pygame

from .sc_widget import SCWidget


# class syntax
class ContainerOrientation(Enum):
    HORIZONTAL = 1 #left to right
    VERTICAL = 2 #top to bottom


class SCContainer(SCWidget):
    def __init__(self, children: List[SCWidget], orientation=ContainerOrientation.HORIZONTAL, inner_padding=5):
        super().__init__()
        self.orientation=orientation
        self.children=[]
        for child in children:
            self.add(child, update=False)
        self.inner_padding=inner_padding
        self.update()

    def add(self, widget, update=True):
        self.children.append(widget)
        widget.parent = self
        if update:
            self.update()

    def update(self):
        sum_x = 0
        sum_y = 0
        max_x = 0
        max_y = 0
        for child in self.children:
            child.update()
            sum_x+=child.get_width()
            sum_y+=child.get_height()
            max_y=max(max_y,child.get_height())
            max_x=max(max_x,child.get_width())
            if child!=self.children[-1]:
                #No element allowed multiple times
                sum_x+=self.inner_padding
                sum_y+=self.inner_padding
        if self.orientation==ContainerOrientation.HORIZONTAL:
            self._height = max_y
            self._width = sum_x
        else:
            self._height = sum_y
            self._width = max_x
        self._surface=pygame.surface.Surface(self.get_size())
        self._surface.fill(pygame.Color('white'))

        pos_val=0
        for child in self.children:
            if self.orientation == ContainerOrientation.HORIZONTAL:
                child.draw(self._surface,(pos_val,0))
                pos_val+=child.get_width()+self.inner_padding
            else:
                child.draw(self._surface,(0,pos_val))
                pos_val+=child.get_height()+self.inner_padding


    def get_height(self):
        return self._height

    def get_width(self):
        return self._width


    def draw(self, screen, location):
        # self.children[0].draw(screen,location)
        x_pos,y_pos=location
        screen.blit(self._surface,pygame.rect.Rect(x_pos,y_pos,self.get_width(),self.get_height()))

