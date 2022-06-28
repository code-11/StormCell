from .scenario import Scenario
from node import Node
from nation import Nation


class TestScenario(Scenario):

    def __init__(self):
        super().__init__()
        red_nation = Nation('red', 'Red')
        blue_nation = Nation('blue', 'Blue')

        self.nations = [red_nation, blue_nation]

        a1 = Node((50, 50), owner=red_nation, build_id='M')
        a2 = Node((80, 20), owner=red_nation, build_id='F')
        a3 = Node((80, 100))
        a4 = Node((120, 100))
        a5 = Node((120, 20), owner=blue_nation, build_id='C')
        a6 = Node((150, 50), owner=blue_nation, build_id='M')

        a1.connect(a2)
        a1.connect(a3)
        a2.connect(a3)

        a4.connect(a5)
        a4.connect(a6)
        a5.connect(a6)

        a3.connect(a4)

        self.nodes = [a1, a2, a3, a4, a5, a6]
