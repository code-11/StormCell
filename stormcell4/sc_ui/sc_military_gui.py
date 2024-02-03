from typing import List

import pygame

from sc_game.military import army
from sc_game.military.army import ArmyStance
from sc_ui.label import Label
from sc_ui.sc_container import ContainerOrientation, SCContainer
from sc_ui.sc_image import SCImage
from sc_ui.sc_selectable_image import SelectableImage
from sc_ui.sc_widget import SCWidget

from functools import partial

from sc_ui.side_bar_state import SideBarState


class ArmyGui(SCContainer):
    def __init__(self, army, game):
        self.army = army
        super().__init__([], game, orientation=ContainerOrientation.HORIZONTAL)

    def update(self, the_game):
        self.children = []
        self.children.append(Label(self.army.nation.name, font_size=12))
        self.children.append(Label(self.army.name, font_size=12))
        self.children.append(Label(str(self.army.size), font_size=12))
        self.children.append(Label(str(self.army.quality), font_size=12))
        self.children.append(Label(str(self.army.stance.to_label()), font_size=12))
        super().update(the_game)

class ControlledArmyGui(SCContainer):
    def __init__(self, army, the_game):
        self.army = army
        super().__init__([], the_game, orientation=ContainerOrientation.VERTICAL)

    def update_army_stance(self, army, stance):
        army.stance = stance
        return SideBarState(should_refresh=True)

    def update_army_stance_movement(self, army, the_game):
        army.stance = ArmyStance.MOVING
        adjacent_regions = the_game.the_map.get_adjacent_regions(army.region)
        return SideBarState(should_refresh=True, other_regions=adjacent_regions)

    def update(self, the_game):
        self.children = [ArmyGui(self.army, the_game)]

        aggressive_icon = SelectableImage.using_name("sword.jpg", size=(17, 17), border_size=1, border_color=pygame.color.Color('black'), selected_size=1, select_color=pygame.color.Color('blue'), padding=1, selected=self.army.stance == ArmyStance.AGGRESSIVE)
        defensive_icon = SelectableImage.using_name("shield.jpg", size=(17, 17), border_size=1, border_color=pygame.color.Color('black'), selected_size=1, select_color=pygame.color.Color('blue'), padding=1, selected=self.army.stance == ArmyStance.DEFENSIVE)
        pacify_icon = SelectableImage.using_name("fist-down.jpg", size=(17, 17), border_size=1, border_color=pygame.color.Color('black'), selected_size=1, select_color=pygame.color.Color('blue'), padding=1, selected=self.army.stance == ArmyStance.PACIFY)
        raiding_icon = SelectableImage.using_name("fire.jpg", size=(17, 17), border_size=1, border_color=pygame.color.Color('black'), selected_size=1, select_color=pygame.color.Color('blue'), padding=1, selected=self.army.stance == ArmyStance.RAIDING)
        guerilla_icon = SelectableImage.using_name("mask.jpg", size=(17, 17), border_size=1, border_color=pygame.color.Color('black'), selected_size=1, select_color=pygame.color.Color('blue'), padding=1, selected=self.army.stance == ArmyStance.GUERILLA)
        move_icon = SelectableImage.using_name("move.jpg", size=(17, 17), border_size=1, border_color=pygame.color.Color('black'), selected_size=1, select_color=pygame.color.Color('blue'), padding=1, selected=self.army.stance == ArmyStance.MOVING)

        aggressive_icon.set_on_click(
           partial(self.update_army_stance, self.army, ArmyStance.AGGRESSIVE)
        )
        defensive_icon.set_on_click(
            partial(self.update_army_stance, self.army, ArmyStance.DEFENSIVE)
        )
        pacify_icon.set_on_click(
            partial(self.update_army_stance, self.army, ArmyStance.PACIFY)
        )
        raiding_icon.set_on_click(
            partial(self.update_army_stance, self.army, ArmyStance.RAIDING)
        )
        guerilla_icon.set_on_click(
            partial(self.update_army_stance, self.army, ArmyStance.GUERILLA)
        )
        move_icon.set_on_click(
            partial(self.update_army_stance_movement, self.army, the_game)
        )

        stance_box = SCContainer([
                aggressive_icon,
                defensive_icon,
                pacify_icon,
                raiding_icon,
                guerilla_icon],
            the_game,
            inner_padding=5)
        stance_box.id = "stance_box"
        stance_and_move_box = SCContainer([
            stance_box,
            move_icon,
        ],the_game, inner_padding=15)
        stance_and_move_box.id = "stance_and_move_box"
        self.children.append(stance_and_move_box)
        super().update(the_game)


class MilitaryGui(SCContainer):
    def __init__(self, screen, game, sidebar_state):
        self.screen = screen
        self.game = game
        self.sidebar_state = sidebar_state
        super().__init__([],game, orientation=ContainerOrientation.VERTICAL)

    def update(self, the_game):
        selected_region = self.sidebar_state.selected_region
        self.children = []
        if selected_region is not None:
            all_regions_to_armies = self.game.the_map.make_region_to_armies_map()
            selected_region_armies = all_regions_to_armies.get(selected_region, [])
            if selected_region_armies:
                self.children.append(Label("Armies", font_size=20))
                for army in selected_region_armies:
                    if self.game.playing_as_country == army.nation:
                        self.add(ControlledArmyGui(army,the_game), update=False)
                    else:
                        self.children.append(ArmyGui(army,the_game))
        super().update(the_game)
