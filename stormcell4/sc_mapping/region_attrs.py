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
    def __init__(self, name, primary_people: People, primary_culture: Culture, primary_religion: Religion, level: int = 1):
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
