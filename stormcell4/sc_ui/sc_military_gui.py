from typing import List

import pygame

from StormCell.stormCell4.sc_game.military import army
from StormCell.stormCell4.sc_game.military.army import ArmyStance
from StormCell.stormCell4.sc_ui.label import Label
from StormCell.stormCell4.sc_ui.sc_container import ContainerOrientation, SCContainer
from StormCell.stormCell4.sc_ui.sc_image import SCImage
from StormCell.stormCell4.sc_ui.sc_selectable_image import SelectableImage
from StormCell.stormCell4.sc_ui.sc_widget import SCWidget

from functools import partial

class ArmyGui(SCContainer):
    def __init__(self, army):
        self.army = army
        super().__init__([], orientation=ContainerOrientation.HORIZONTAL)

    def update(self):
        self.children = []
        self.children.append(Label(self.army.nation.name, font_size=12))
        self.children.append(Label(self.army.name, font_size=12))
        self.children.append(Label(str(self.army.size), font_size=12))
        self.children.append(Label(str(self.army.quality), font_size=12))
        self.children.append(Label(str(self.army.stance.to_label()), font_size=12))
        super().update()

class ControlledArmyGui(SCContainer):
    def __init__(self, army):
        self.army = army
        super().__init__([], orientation=ContainerOrientation.VERTICAL)

    def update_army_stance(self, army, stance):
        army.stance = stance
        return True

    def update(self):
        self.children = [ArmyGui(self.army)]

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

        stance_box = SCContainer([
                aggressive_icon,
                defensive_icon,
                pacify_icon,
                raiding_icon,
                guerilla_icon],
            inner_padding=5)
        stance_and_move_box = SCContainer([
            stance_box,
            move_icon
        ], inner_padding=15)
        self.children.append(stance_and_move_box)
        super().update()


class MilitaryGui(SCContainer):
    def __init__(self, screen, game, sidebar_state):
        self.screen = screen
        self.game = game
        self.sidebar_state = sidebar_state
        super().__init__([], orientation=ContainerOrientation.VERTICAL)

    def update(self):
        selected_region = self.sidebar_state.selected_region
        self.children = []
        if selected_region is not None:
            all_regions_to_armies = self.game.the_map.make_region_to_armies_map()
            selected_region_armies = all_regions_to_armies.get(selected_region, [])
            if selected_region_armies:
                self.children.append(Label("Armies", font_size=20))
                for army in selected_region_armies:
                    if self.game.playing_as_country == army.nation:
                        self.add(ControlledArmyGui(army), update=False)
                    else:
                        self.children.append(ArmyGui(army))
        super().update()
