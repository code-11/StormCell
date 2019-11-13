import clock


class Game (object):
    country_list = []
    events = []
    history = []

    game_clock = None

    def __init__(self):
        self.game_clock = clock.Clock()
        self.player_list = []

    def add_player(self, player):
        self.player_list.append(player)