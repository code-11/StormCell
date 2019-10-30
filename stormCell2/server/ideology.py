class Spirit:
    def __init__(self, demos, speed, cleric, market, peace, tolerance, peeps):
        self.demos = demos
        self.speed = speed
        self.cleric = cleric
        self.market = market
        self.peace = peace
        self.tolerance = tolerance
        self.peeps = peeps


Spirit.AmericanSpirit = Spirit(demos=.75, speed=.4, cleric=.5, market=.5, peace=.5, tolerance=.3, indiv=.9)
Spirit.EuropeanSpirit = Spirit(demos=.85, speed=.45, cleric=.6, market=.5, peace=.8, tolerance=.4, indiv=.9)
Spirit.RussiaSpirit = Spirit(demos=.2, speed=.4, cleric=0, market=.1, peace=.2, tolerance=.1, indiv=.1)

