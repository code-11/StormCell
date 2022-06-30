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

    def click_test(self, mouse):
        for node in self.nodes:
            if node.is_clicked(mouse):
                return node

    def get_playing_nation(self):
        _, nation_index = self.turn
        return self.nations[nation_index]

    def get_longest_turn_text(self):
        _, longest_nation_name = max(map(lambda nation: (len(nation.name), nation.name), self.nations))
        return f"Turn 00000: {longest_nation_name}"

    def get_cur_turn_text(self):
        major_turn, _ = self.turn
        playing_nation = self.get_playing_nation()
        return f"Turn {major_turn}: {playing_nation.name}"

    def possibly_build_at_node(self, node, build_id):
        if node is None:
            return

        is_clear = node.building is None

        playing_nation = self.get_playing_nation()
        owner_matches_playing_nation = playing_nation is node.owner

        if is_clear and owner_matches_playing_nation:
            node.set_build_id(build_id)
