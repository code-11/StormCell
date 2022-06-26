import pygame, sys
from pygame.locals import *


class Nation(object):
    def __init__(self, color, name):
        self.color = color
        self.name = name


class Node(object):
    def __init__(self, location, owner=None):
        self.edges = []
        self.armies = []
        self.owner = owner
        self.location = location

    def connect(self, other_node):
        self.edges.append(other_node)
        other_node.edges.append(self)

    def draw_connection(self, window, other_node):
        pygame.draw.line(window, 'white', self.location, other_node.location, width=2)

    def draw_connections(self,window):
        for edge in self.edges:
            self.draw_connection(window, edge)

    def draw_node(self, window):
        if self.owner is not None:
            pygame.draw.circle(window, self.owner.color, center=self.location, radius=13)
        pygame.draw.circle(window, 'white', center=self.location, radius=15, width=2)



class Scenario(object):

    def __init__(self):
        super().__init__()


class TestScenario(Scenario):

    def __init__(self):
        super().__init__()
        red_nation = Nation('red', 'Red')
        blue_nation = Nation('blue', 'Blue')

        self.nations = [red_nation, blue_nation]

        a1 = Node((50, 50), owner=red_nation)
        a2 = Node((80, 20), owner=red_nation)
        a3 = Node((80, 100))
        a4 = Node((120, 100))
        a5 = Node((120, 20), owner=blue_nation)
        a6 = Node((150, 50), owner=blue_nation)

        a1.connect(a2)
        a1.connect(a3)
        a2.connect(a3)

        a4.connect(a5)
        a4.connect(a6)
        a5.connect(a6)

        a3.connect(a4)

        self.nodes = [a1, a2, a3, a4, a5, a6]


def run():
    pygame.init()
    window = pygame.display.set_mode((400, 300))
    pygame.display.set_caption('StormCell3')
    scenario = TestScenario()
    while True:  # main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        for node in scenario.nodes:
            node.draw_connections(window)
        for node in scenario.nodes:
            node.draw_node(window)
        pygame.display.update()


if __name__ == '__main__':
    run()
