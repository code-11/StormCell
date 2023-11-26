from typing import Optional, Tuple
from enum import Enum

import pygame

from StormCell.stormCell4.sc_mapping.region_geometry import RegionGeometry


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
    ICE = None
    TUNDRA = None
    WOODS = None
    HILLS = None
    FOREST = None
    PLAINS = None
    DESERT = None
    COAST = None
    GRASSLANDS = None
    MOUNTAINS = None
    SWAMP = None

    def __init__(self, name, color, defensiveness, mobility, attrition):
        self.name = name
        self.color = color
        self.defensiveness = defensiveness  # multiplier
        self.mobility = mobility  # multiplier
        self.attrition = attrition  # multiplier


Terrain.MOUNTAINS = Terrain("Mountains", "#362910", 2, .1, 1.3)
Terrain.COAST = Terrain("Coast", "#ffd282", 1, 1, 1.1)
Terrain.GRASSLANDS = Terrain("Grasslands", "#3ec453", 1, 1, 1)
Terrain.PLAINS = Terrain("Plains", "#aa9161", .7, 1.5, 1.2)
Terrain.DESERT = Terrain("Desert", "#d08f55", .5, 1.6, 5)
Terrain.SWAMP = Terrain("Swamp", "#2c3e26", 1.5, .2, 4)
Terrain.HILLS = Terrain("Hills", "#636200", 1.7, .4, 1)
Terrain.WOODS = Terrain("Woods", "#29661e", 1.5, .4, 1)
Terrain.FOREST = Terrain("Forest", "#14430c", 1.7, .3, 1.1)
Terrain.TUNDRA = Terrain("Tundra", "#53774d", .5, .9, 4)
Terrain.ICE = Terrain("Ice", "#dad2af", .5, .6, 6)


class People(object):
    def __init__(self, name, culture: Culture, religion: Religion, ebang: float, magic: float, religiousness: float,
                 tradition: float):
        self.name = name
        self.religiousness = religiousness
        self.magic = magic
        self.ebang = ebang
        self.religion = religion
        self.culture = culture
        self.tradition = tradition

    def __str__(self):
        return str(self.__dict__)

    def to_pop(self, number, disease=0.0):
        Pop(
            number=number,
            culture=self.culture,
            religion=self.religion,
            ebang=self.ebang,
            magic=self.magic,
            disease=disease,
        )


class Nation(object):
    def __init__(self, name, primary_people: Optional[People], primary_culture: Optional[Culture],
                 primary_religion: Optional[Religion], level: int = 1):
        self.primary_people = primary_people
        self.primary_culture = primary_culture
        self.primary_religion = primary_religion
        self.level = level
        self.name = name

    def __str__(self):
        return self.name


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
    def __init__(self, name):
        self.name = name
        self.resources: dict[Resource:float] = {}
        self.pops = []
        self.geometry: Optional[RegionGeometry] = None
        self.terrain = Terrain.GRASSLANDS

    @property
    def tile_num(self):
        return int(self.name.rsplit("L", 1)[1])

    def draw(self, screen, fill_color: Optional[Tuple[float, float, float]], edge_color: Optional[Tuple[float, float, float]]):
        for poly in self.geometry.polys:
            if edge_color:
                pygame.draw.polygon(screen, edge_color, poly, width=5)
            if fill_color:
                pygame.draw.polygon(screen, fill_color, poly, width=0)
