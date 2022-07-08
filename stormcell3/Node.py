from math import floor, ceil

import pygame
from building import Building

NODE_WIDTH = 45


class Node(object):
    cur_id = 0

    def __init__(self, location, owner=None, build_id=''):
        self.id = Node.cur_id
        Node.cur_id += 1
        self.edges = []
        self.owner = owner
        self.location = location
        self.building = Building.construct(build_id)
        self.army = 0
        self.moved_army = 0

    def set_build_id(self, build_id):
        self.building = Building.construct(build_id)

    def set_owner_build_id(self, owner, build_id):
        self.owner = owner
        self.set_build_id(build_id)

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

    def is_clicked(self, mouse):
        return self.get_rect().collidepoint(mouse)

    def draw_as_selected(self, window):
        selected_loc = (self.location[0] - 6, self.location[1] - 6)
        pygame.draw.rect(window, 'green', pygame.Rect(selected_loc, (NODE_WIDTH + 12, NODE_WIDTH + 12)), width=2)

    def undraw_as_selected(self, window):
        selected_loc = (self.location[0] - 6, self.location[1] - 6)
        pygame.draw.rect(window, 'black', pygame.Rect(selected_loc, (NODE_WIDTH + 12, NODE_WIDTH + 12)))

    def draw_node(self, window, font):
        # Draw outer edge and inner color. We want this first so that the text is atop it.
        fill_color = 'black' if self.owner is None else self.owner.color
        pygame.draw.rect(window, fill_color, pygame.Rect(self.location, (NODE_WIDTH, NODE_WIDTH)))
        pygame.draw.rect(window, 'white', pygame.Rect(self.location, (NODE_WIDTH + 1, NODE_WIDTH + 1)), width=1)

        # Draw building and army values
        if self.army != 0 or self.moved_army != 0:
            army_text = ("" if self.army == 0 else str(self.army)) + (
                "" if self.moved_army == 0 else f"({self.moved_army})")
            mid_bottom = self.get_rect().midbottom
            text_surf, _ = font.render(army_text, True, 'white')
            text_rect = text_surf.get_rect()
            army_draw_location = mid_bottom[0] - text_rect.width // 2, mid_bottom[1] - (text_rect.height + 3)
            font.render_to(window, army_draw_location, army_text, 'white')

        if self.building is not None:
            top_left = self.get_rect().topleft
            building_draw_location = (top_left[0] + 3, top_left[1] + 3)
            self.building.draw_building(window, building_draw_location, font)

    def has_edge(self, other_node):
        return other_node in self.edges

    def move_army(self, other_node):
        other_node.moved_army = self.army
        other_node.owner = self.owner
        self.army = 0

    def attack_move_army(self, other_node):
        total_defending_army = other_node.army + other_node.moved_army
        # Positive is attacker win, negative is defender
        fort_mult = 1.5 if other_node.building is not None and other_node.building.abbreviation == 'F' else 1
        diff = floor(self.army - (total_defending_army * fort_mult))
        if diff > 0:
            # Win
            other_node.army = 0
            other_node.moved_army = diff
            other_node.owner = self.owner
            # TODO: Interesting decision, do buildings get destroyed? Yes for now.
            other_node.building = None
            self.army = 0
        else:
            # Lose
            other_node.army = 0
            # Survivors
            other_node.moved_army = ceil(total_defending_army - (self.army * (1 / fort_mult)))
            self.army = 0

    def sc_json_save(self):
        return {
            "id": self.id,
            "edges": [edge.id for edge in self.edges],
            "owner": self.owner.name if self.owner is not None else "",
            "location": self.location,
            "building": self.building.abbreviation if self.building is not None else "",
            "army": self.army,
            "moved_army": self.moved_army
        }