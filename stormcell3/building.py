class Building(object):

    @classmethod
    def construct(cls, abbreviation):
        if abbreviation == 'F':
            return Fort()
        elif abbreviation == 'M':
            return Manufactory()
        elif abbreviation == 'C':
            return City()
        else:
            return None

    def __init__(self):
        self.abbreviation = ''
        self.name = ''

    def defence_bonus(self):
        return 0

    def do_action(self, scenario):
        return

    def draw_building(self, window, location, font):
        font.render_to(window, location, self.abbreviation, 'white')


class Fort(Building):
    def __init__(self, ):
        super().__init__()
        self.abbreviation = 'F'
        self.name = "Fort"

    def defence_bonus(self):
        return 2


class City(Building):
    def __init__(self, ):
        super().__init__()
        self.abbreviation = 'C'
        self.name = "City"

    def do_action(self, scenario):
        # Provide money
        pass


class Manufactory(Building):
    def __init__(self, ):
        super().__init__()
        self.abbreviation = 'M'
        self.name = "Manufactory"

    def do_action(self, scenario):
        # Provide units
        pass
