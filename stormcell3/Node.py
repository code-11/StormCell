import pygame
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

    def draw_connections(self, window):
        for edge in self.edges:
            self.draw_connection(window, edge)

    def draw_node(self, window):
        if self.owner is not None:
            pygame.draw.circle(window, self.owner.color, center=self.location, radius=13)
        pygame.draw.circle(window, 'white', center=self.location, radius=15, width=2)
