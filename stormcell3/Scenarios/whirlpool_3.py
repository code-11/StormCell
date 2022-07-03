import math

from Scenarios.scenario import Scenario
from Scenarios.scenario_creation_util import *
from nation import Nation


def _arm_locs():
    return [(3, 3), (2, 4), (1, 5), (2, 6), (3, 7), (4, 7), (4, 6)]


def _arm_conns():
    return [((3, 3), (2, 4)), ((2, 4), (1, 5)), ((1, 5), (2, 6)), \
            ((2, 6), (3, 7)), ((3, 7), (4, 7)), ((3, 7), (4, 6)),
            ((4, 7), (4, 6))]


class Whirlpool3(Scenario):

    def __init__(self):
        super().__init__()
        red_nation = Nation('darkred', 'Red', starting_gold=30)
        blue_nation = Nation('blue', 'Blue', starting_gold=30)
        green_nation = Nation('darkgreen', 'Green', starting_gold=30)
        self.nations = [red_nation, blue_nation, green_nation]

        arm1 = _arm_locs()
        arm2 = rotate_locs((3, 3), _arm_locs(), (2 * math.pi / 3))
        arm3 = rotate_locs((3, 3), _arm_locs(), (4 * math.pi / 3))

        all_locs = uniq(arm1 + arm2 + arm3)

        self.nodes = nodify(yshift_locs(xshift_locs(mult_locs(all_locs, 60), 150), 50))

        arm1_conns = _arm_conns()
        arm2_conns = rotate_conns((3, 3), _arm_conns(), (2 * math.pi / 3))
        arm3_conns = rotate_conns((3, 3), _arm_conns(), (4 * math.pi / 3))

        all_conns = uniq(arm1_conns + arm2_conns + arm3_conns)

        connectify(self.nodes, yshift_conns(xshift_conns(mult_conns(all_conns, 60), 150), 50))

        loc_node_map = {node.location: node for node in self.nodes}

        def loc_to_node(loc):
            return loc_node_map.get(yshift(xshift(mult(loc, 60), 150), 50), None)

        a1 = loc_to_node((4, 6))
        a2 = loc_to_node(rotate((3, 3), (4, 6), 2 * math.pi / 3))
        a3 = loc_to_node(rotate((3, 3), (4, 6), 4 * math.pi / 3))
        a1.set_owner_build_id(red_nation, "C")
        a1.army=3
        a2.set_owner_build_id(blue_nation, "C")
        a2.army = 3
        a3.set_owner_build_id(green_nation, "C")
        a3.army = 3
