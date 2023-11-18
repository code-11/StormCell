from typing import List

from StormCell.stormCell4.sc_game.military import army
from StormCell.stormCell4.sc_game.military.army import ArmyStance
from StormCell.stormCell4.sc_ui.label import Label
from StormCell.stormCell4.sc_ui.sc_container import ContainerOrientation, SCContainer
from StormCell.stormCell4.sc_ui.sc_image import SCImage
from StormCell.stormCell4.sc_ui.sc_widget import SCWidget


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

    def update_army_stance(self,army, stance):
        army.stance = stance

    def update(self):
        self.children = [ArmyGui(self.army)]
        aggressive_icon = SCImage.using_name("sword.jpg", size=(17, 17), border_size=1)
        defensive_icon = SCImage.using_name("shield.jpg", size=(17, 17), border_size=1)
        pacify_icon = SCImage.using_name("fist-down.jpg", size=(17, 17), border_size=1)
        raiding_icon = SCImage.using_name("fire.jpg", size=(17, 17), border_size=1)
        guerilla_icon = SCImage.using_name("mask.jpg", size=(17, 17), border_size=1)

        aggressive_icon.set_on_click(
            lambda: self.update_army_stance(self.army, ArmyStance.AGGRESSIVE)
        )
        defensive_icon.set_on_click(
            lambda: self.update_army_stance(self.army, ArmyStance.DEFENSIVE)
        )
        pacify_icon.set_on_click(
            lambda: self.update_army_stance(self.army, ArmyStance.PACIFY)
        )
        raiding_icon.set_on_click(
            lambda: self.update_army_stance(self.army, ArmyStance.RAIDING)
        )
        guerilla_icon.set_on_click(
            lambda: self.update_army_stance(self.army, ArmyStance.GUERILLA)
        )

        icons_box = SCContainer([
                aggressive_icon,
                defensive_icon,
                pacify_icon,
                raiding_icon,
                guerilla_icon],
            inner_padding=5)
        self.children.append(icons_box)
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
                        self.children.append(ControlledArmyGui(army))
                    else:
                        self.children.append(ArmyGui(army))
        super().update()
