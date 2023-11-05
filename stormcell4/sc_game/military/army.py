from dataclasses import dataclass
from enum import Enum
from typing import Optional

from StormCell.stormCell4.sc_mapping.region_attrs import Region


class ArmyStance(Enum):
    AGGRESSIVE = 1
    DEFENSIVE = 2
    PACIFY = 3
    RAIDING = 4
    GUERILLA = 5


@dataclass
class Army(object):
    name: str
    size: int
    quality: float  # 0-100
    general_quality: float  # 0-100


class ArmyStatus(object):
    def __init__(self, army: Army, stance: ArmyStance, region: Optional[Region]):
        self.army = army
        self.stance = stance
        self.region = region
