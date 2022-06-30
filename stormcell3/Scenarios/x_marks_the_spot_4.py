import math

from .scenario import Scenario
from .scenario_creation_util import *
from node import Node
from nation import Nation


# Represent the connections as points that exist between two nodes
def _corner_conns():
    return [((0, 0), (1, 0)), ((1, 0), (2, 0)), ((0, 0), (0, 1)), ((0, 1), (1, 0)), ((2, 0), (2, 1)), ((2, 0), (3, 1)),
            ((1, 0), (2, 1)), ((0, 1), (2, 1)), ((2, 1), (3, 1)), ((3, 0), (3, 1)), ((3, 1), (4, 1)),
            ((0, 1), (0, 2)), ((0, 1), (1, 2)), ((1, 0), (1, 2)), ((2, 1), (1, 2)),
            ((0, 2), (1, 2)), ((0, 2), (1, 3)), ((1, 2), (1, 3)), ((1, 3), (1, 4)),
            ((0, 3), (1, 3)), ((2, 1), (3, 3)), ((1, 2), (3, 3)), ((3, 3), (4, 4))]


def _corner_locs():
    temp_locs = set()
    for i in range(4):
        for j in range(4):
            temp_locs.add((i, j))
    temp_locs.remove((1, 1))
    temp_locs.remove((2, 2))
    temp_locs.remove((3, 2))
    temp_locs.remove((2, 3))

    temp_locs.add((1, 4))
    temp_locs.add((3, 3))
    temp_locs.add((4, 1))
    temp_locs.add((4, 4))
    return list(temp_locs)


class XMarksTheSpot4(Scenario):

    def __init__(self):
        super().__init__()
        red_nation = Nation('darkred', 'Red')
        blue_nation = Nation('blue', 'Blue')
        green_nation = Nation('darkgreen', 'Green')
        purple_nation = Nation('purple', 'Purple')

        self.nations = [red_nation, blue_nation, green_nation, purple_nation]

        # Create locations
        top_left = _corner_locs()
        top_right = x_mirror_locs(_corner_locs(), 8)

        top_half = top_left + top_right
        bottom_half = y_mirror_locs(top_half, 8)

        all_locs = uniq(bottom_half + top_half)

        # self.nodes = _nodify(all_locs) # For debugging missing nodes
        self.nodes = nodify(yshift_locs(xshift_locs(mult_locs(all_locs, 60), 5), 5))

        # Create connections
        top_left = _corner_conns()
        top_right = x_mirror_conns(_corner_conns(), 8)

        top_half = top_left + top_right
        bottom_half = y_mirror_conns(top_half, 8)

        all_conns = uniq(bottom_half + top_half)
        # _connectify(self.nodes, all_conns) # For debugging missing nodes
        connectify(self.nodes, yshift_conns(xshift_conns(mult_conns(all_conns, 60), 5), 5))

        loc_node_map = {node.location: node for node in self.nodes}

        def loc_to_node(loc):
            return loc_node_map.get(yshift(xshift(mult(loc, 60), 5), 5), None)

        a1 = loc_to_node((0, 0))
        a2 = loc_to_node((1, 0))
        a3 = loc_to_node((0, 1))
        a1.set_owner_build_id(red_nation, "F")
        a2.set_owner_build_id(red_nation, "M")
        a3.set_owner_build_id(red_nation, "C")
        a1.army = 3


        b1 = loc_to_node((8, 0))
        b2 = loc_to_node((7, 0))
        b3 = loc_to_node((8, 1))
        b1.set_owner_build_id(blue_nation, "F")
        b2.set_owner_build_id(blue_nation, "M")
        b3.set_owner_build_id(blue_nation, "C")
        b1.army = 3

        c1 = loc_to_node((8, 8))
        c2 = loc_to_node((7, 8))
        c3 = loc_to_node((8, 7))
        c1.set_owner_build_id(green_nation, "F")
        c2.set_owner_build_id(green_nation, "M")
        c3.set_owner_build_id(green_nation, "C")
        c1.army = 3

        d1 = loc_to_node((0, 8))
        d2 = loc_to_node((0, 7))
        d3 = loc_to_node((1, 8))
        d1.set_owner_build_id(purple_nation, "F")
        d2.set_owner_build_id(purple_nation, "M")
        d3.set_owner_build_id(purple_nation, "C")
        d1.army = 3
