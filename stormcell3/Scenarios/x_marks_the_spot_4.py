from .scenario import Scenario
from node import Node
from nation import Nation


#Represent the connections as points that exist between two nodes

def _corner():
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
    return list(temp_locs)

def _mult(tupes,scalar):
    return [(tupx * scalar, tupy * scalar) for tupx, tupy in tupes]

def _xshift(tupes, val):
    return [(tupx +val, tupy) for tupx, tupy in tupes]

def _yshift(tupes, val):
    return [(tupx, tupy + val) for tupx, tupy in tupes]

def _x_mirror(tupes, max_x_i):
    return [(max_x_i-tupx, tupy) for tupx, tupy in tupes]

def _y_mirror(tupes, max_y_i):
    return [(tupx, max_y_i-tupy) for tupx, tupy in tupes]

def _nodify(tupes):
    return [Node(tup) for tup in tupes]

def _uniq(tupes):
    return list(set(tupes))

class XMarksTheSpot4(Scenario):

    def __init__(self):
        super().__init__()
        red_nation = Nation('red', 'Red')
        blue_nation = Nation('blue', 'Blue')
        green_nation = Nation('green', 'Green')
        purple_nation = Nation('purple', 'Purple')

        self.nations = [red_nation, blue_nation, green_nation, purple_nation]

        top_left = _corner()
        top_right = _x_mirror(_corner(), 8)

        top_half = top_left+top_right
        bottom_half = _y_mirror(top_half, 8)

        all_tups = _uniq(bottom_half + top_half)

        self.nodes = _nodify(_yshift(_xshift(_mult(all_tups,60),5),5))
