import pygame

from building import Building

NODE_WIDTH = 30


class Node(object):
    def __init__(self, location, owner=None, build_id=''):
        self.edges = []
        self.armies = []
        self.owner = owner
        self.location = location
        self.building = Building.construct(build_id)
        self.army = 0

    def connect(self, other_node):
        self.edges.append(other_node)
        other_node.edges.append(self)

    def get_rect(self):
        return pygame.Rect(self.location, (NODE_WIDTH, NODE_WIDTH))

    def draw_connection(self, window, other_node):
        this_rect = self.get_rect()
        other_rect = other_node.get_rect()
        pygame.draw.line(window, 'white', this_rect.center, other_rect.center, width=2)

    def draw_connections(self, window):
        for edge in self.edges:
            self.draw_connection(window, edge)

    def draw_node(self, window, font):
        # Draw outer edge and inner color. We want this first so that the text is atop it.
        if self.owner is not None:
            pygame.draw.rect(window, self.owner.color, pygame.Rect(self.location, (NODE_WIDTH, NODE_WIDTH)))
        pygame.draw.rect(window, 'white', pygame.Rect(self.location, (NODE_WIDTH + 1, NODE_WIDTH + 1)), width=1)

        # Draw building and army values
        if self.owner is not None and self.building is not None:

            top_left = self.get_rect().topleft
            building_draw_location = (top_left[0] + 3, top_left[1] + 3)
            self.building.draw_building(window, building_draw_location, font)

            army_text = str(self.army)
            mid_bottom = self.get_rect().midbottom
            text_surf, _ = font.render(army_text, True, 'white')
            text_rect = text_surf.get_rect()
            army_draw_location = mid_bottom[0] - text_rect.width//2 , mid_bottom[1] - (text_rect.height + 3)
            font.render_to(window, army_draw_location, army_text, 'white')


