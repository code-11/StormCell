import copy
import functools
from dataclasses import dataclass, field
from typing import Optional, List

from sc_mapping.region_attrs import Region


def custom_or(a, b):
    if a is True or b is True:
        return True
    elif a is not None and b is None:
        return a
    elif b is not None and a is None:
        return b
    else:
        return False

@dataclass
class SideBarState:
    selected_region: Optional[Region] = None
    should_refresh: bool = False
    other_regions: List[Region]=field(default_factory=list)

    @staticmethod
    def glom_func(state_a, state_b):
        if state_a is None and state_b is not None:
            return state_b
        elif state_a is not None and state_b is None:
            return state_a
        elif state_a is not None and state_b is not None:
            return SideBarState(
                state_a.selected_region if state_a.selected_region is not None else state_b.selected_region,
                custom_or(state_a.should_refresh, state_b.should_refresh),
                state_a.other_regions if len(state_a.other_regions) > 0 else state_b.other_regions)
        else:
            print("HUH?")

    @classmethod
    def glom(cls, arr):
        return functools.reduce(cls.glom_func, arr)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"SBS({self.selected_region},{self.should_refresh},{self.other_regions})"
