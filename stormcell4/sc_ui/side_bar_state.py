from dataclasses import dataclass
from typing import Optional

from StormCell.stormCell4.sc_mapping.region_attrs import Region


@dataclass
class SideBarState:
    selected_region: Optional[Region] = None
