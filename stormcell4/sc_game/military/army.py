from dataclasses import dataclass
from enum import Enum
from typing import Optional

from sc_mapping.region_attrs import Region, Nation


class ArmyStance(Enum):
    AGGRESSIVE = 1
    DEFENSIVE = 2
    PACIFY = 3
    RAIDING = 4
    GUERILLA = 5
    MOVING = 6

    def to_label(self):
        return {
            ArmyStance.AGGRESSIVE: "Aggressisve",
            ArmyStance.DEFENSIVE: "Defensive",
            ArmyStance.PACIFY: "Pacify",
            ArmyStance.RAIDING: "Raiding",
            ArmyStance.GUERILLA: "Guerilla",
            ArmyStance.MOVING: "Moving",
        }.get(self, "")


@dataclass
class Army(object):
    name: str
    size: int
    quality: float  # 0-100
    general_quality: float  # 0-100
    region: Region
    nation: Nation
    stance: ArmyStance = ArmyStance.AGGRESSIVE
