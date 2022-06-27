class Scenario(object):

    def __init__(self):
        super().__init__()
        self.turn = (0, 0)
        self.nations = []
        self.nodes = []

    def incr_turn(self):
        major_turn, nation_index = self.turn
        if nation_index == len(self.nations) - 1:
            self.turn = (major_turn + 1, 0)
        else:
            self.turn = (major_turn, nation_index + 1)
