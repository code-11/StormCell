from building import Building
import json


class Scenario(object):

    def __init__(self):
        super().__init__()
        self.turn = (0, 0)
        self.nations = []
        self.nodes = []
        self.defeated = {}  # nation name string to boolean
        self.winning_nation = None

    def set_all_undefeated(self):
        self.defeated = {nation.name: False for nation in self.nations}

    def evaluate_buildings(self, nation):
        cities = []
        manufactory_nodes = []
        for node in self.nodes:
            if node.owner is nation and node.building is not None:
                if node.building.abbreviation == 'C':
                    cities.append(node.building)
                elif node.building.abbreviation == 'M':
                    manufactory_nodes.append(node)
        for city in cities:
            nation.gold += 4

        for manufactory_node in manufactory_nodes:
            if nation.gold >= 4:
                nation.gold -= 4
                manufactory_node.army += 1

    def refresh_all_armies(self, nation):
        for node in self.nodes:
            if node.owner is nation and node.moved_army > 0:
                node.army += node.moved_army
                node.moved_army = 0

    def get_winning_nation(self):
        is_alive = lambda nation_name: not self.defeated[nation_name]
        alive_nations = list(filter(is_alive, self.defeated.keys()))
        if len(alive_nations) == 1:
            for nation in self.nations:
                if nation.name == alive_nations[0]:
                    return nation
            return
        else:
            return None

    def defeat_check(self, nation):
        for node in self.nodes:
            if node.owner is nation:
                return False
        return True

    def incr_turn(self):
        major_turn, nation_index = self.turn
        if nation_index == len(self.nations) - 1:
            self.turn = (major_turn + 1, 0)
        else:
            self.turn = (major_turn, nation_index + 1)

        playing_nation = self.get_playing_nation()
        self.refresh_all_armies(playing_nation)
        self.evaluate_buildings(playing_nation)
        if self.defeated[playing_nation.name] or self.defeat_check(playing_nation):
            self.defeated[playing_nation.name] = True
            self.incr_turn()

    def incr_turn_and_check_for_end(self):
        self.incr_turn()
        possible_winning_nation = self.get_winning_nation()
        if possible_winning_nation is not None:
            self.winning_nation = possible_winning_nation

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

    def possibly_destroy_build_at_node(self, node):
        if node is None:
            return

        has_building = node.building is not None

        playing_nation = self.get_playing_nation()
        owner_matches_playing_nation = playing_nation is node.owner

        if has_building and owner_matches_playing_nation:
            node.building = None

    def possibly_build_at_node(self, node, build_id):
        if node is None:
            return

        is_clear = node.building is None

        playing_nation = self.get_playing_nation()
        owner_matches_playing_nation = playing_nation is node.owner

        building_cost = Building.construct(build_id).cost()
        has_enough_money = playing_nation.gold >= building_cost

        if is_clear and owner_matches_playing_nation and has_enough_money:
            node.set_build_id(build_id)
            playing_nation.gold -= building_cost

    def move_command(self, source_node, destination_node):
        playing_nation = self.get_playing_nation()
        source_node_matches_playing_nation = playing_nation is source_node.owner

        source_node_has_army = source_node.army > 0

        destination_node_is_one_away = source_node.has_edge(destination_node)

        if source_node_matches_playing_nation \
                and source_node_has_army \
                and destination_node_is_one_away:

            if destination_node.owner is not source_node.owner:
                # Combat!
                source_node.attack_move_army(destination_node)
            else:
                source_node.move_army(destination_node)

    def sc_json_save(self):
        turn1, turn2 = self.turn
        return json.dumps({
            "turn1": turn1,
            "turn2": turn2,
            "nations": [
                nation.sc_json_save() for nation in self.nations
            ],
            "nodes": [
                node.sc_json_save() for node in self.nodes
            ],
            "defeated": self.defeated
        })
