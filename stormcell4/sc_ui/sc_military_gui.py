from typing import List

from StormCell.stormCell4.sc_ui.label import Label
from StormCell.stormCell4.sc_ui.sc_container import ContainerOrientation, SCContainer
from StormCell.stormCell4.sc_ui.sc_widget import SCWidget


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
                    self.children.append(Label(army.name, font_size=12))
        super().update()
