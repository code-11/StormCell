class Country(object):
    def __init__(self, name):
        self.name = name
        self.continent = None


    def set_continent(self, continent):
        self.continent = continent