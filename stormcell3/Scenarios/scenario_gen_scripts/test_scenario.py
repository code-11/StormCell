from core.scenario import Scenario
from core.node import Node
from core.nation import Nation


class TestScenario(Scenario):

    def __init__(self):
        super().__init__()
        self.name = 'Test scenario 2'
        self.max_players = 2
        red_nation = Nation('red', 'Red')
        blue_nation = Nation('blue', 'Blue')

        self.nations = [red_nation, blue_nation]

        self.set_all_undefeated()

        a1 = Node((50, 100), owner=red_nation, build_id='M')
        a2 = Node((120, 20), owner=red_nation, build_id='F')
        a3 = Node((120, 150))
        a4 = Node((180, 150))
        a5 = Node((180, 20), owner=blue_nation, build_id='C')
        a6 = Node((250, 100), owner=blue_nation, build_id='M')

        a1.connect(a2)
        a1.connect(a3)
        a2.connect(a3)

        a4.connect(a5)
        a4.connect(a6)
        a5.connect(a6)

        a3.connect(a4)

        self.nodes = [a1, a2, a3, a4, a5, a6]
