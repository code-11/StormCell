from typing import Optional
from enum import Enum

import pygame
class Resource(object):
    def __init__(self, name):
        self.name = name


class Culture(object):
    def __init__(self, name, short):
        self.name = name
        self.short = short

    def __repr__(self):
        return self.short

class Religion(object):
    _index = 1
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    @staticmethod
    def auto_mk():
        ind = Religion._index
        Religion._index += 1
        return Religion(f"R{ind}")


class Terrain(object):

    def __init__(self,name,color):
        self.name=name
        self.color=color

Terrain.MOUNTAINS=Terrain("Mountains","#362910")
Terrain.COAST=Terrain("Coast","#ffd282")
Terrain.GRASSLANDS=Terrain("Grasslands","#3ec453")
Terrain.PLAINS = Terrain("Plains", "#aa9161")
Terrain.DESERT = Terrain("Desert", "#d08f55")
Terrain.SWAMP = Terrain("Swamp", "#2c3e26")
Terrain.HILLS = Terrain("Hills", "#636200")
Terrain.WOODS = Terrain("Woods", "#29661e")
Terrain.FOREST = Terrain("Forest", "#14430c")
Terrain.TUNDRA = Terrain("Tundra", "#53774d")
Terrain.ICE = Terrain("Ice", "#dad2af")


class People(object):
    def __init__(self, name, culture: Culture, religion: Religion, ebang: float, magic: float, religiousness: float,
                 tradition: float):
        self.name=name
        self.religiousness = religiousness
        self.magic = magic
        self.ebang = ebang
        self.religion = religion
        self.culture = culture
        self.tradition = tradition

    def __str__(self):
        return str(self.__dict__)

    def to_pop(self,number,disease=0.0):
        Pop(
            number=number,
            culture=self.culture,
            religion=self.religion,
            ebang=self.ebang,
            magic=self.magic,
            disease=disease,
        )


class Nation(object):
    def __init__(self, name, primary_people: Optional[People], primary_culture: Optional[Culture], primary_religion: Optional[Religion], level: int = 1):
        self.primary_people = primary_people
        self.primary_culture = primary_culture
        self.primary_religion = primary_religion
        self.level = level

class Pop(object):
    def __init__(self, number: int, culture: Culture, religion: Religion, ebang: float, magic: float, disease: float):
        self.disease = disease
        self.magic = magic
        self.ebang = ebang
        self.number = number
        self.culture = culture
        self.religion = religion
        self.support = 1


class Region(object):
    def __init__(self,name):
        self.name=name
        self.resources: dict[Resource:float] = {}
        self.pops = []
        self.geometry=None

    @property
    def tile_num(self):
        return int(self.name.rsplit("L",1)[1])


    def draw(self, screen, fill_color, edge_color):
        for poly in self.geometry.polys:
            pygame.draw.polygon(screen, edge_color , poly, width=5)
            pygame.draw.polygon(screen, fill_color, poly, width=0)
