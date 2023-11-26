from .army import ArmyStance, Army


from StormCell.stormCell4.sc_mapping.region_attrs import Terrain, Region

ATK_II = 5
ATK_I = 4
ATK = 3
NEUTRAL = 1  # atk needs 1:1
DEF = .33  # atk needs 3:1
DEF_I = .25  # atk needs 4:1
DEF_II = .2  # atk needs 5:1

# Outer layer is attacker
STANCE_MULT_TABLE = {
    ArmyStance.AGGRESSIVE: {
        ArmyStance.AGGRESSIVE: NEUTRAL,
        ArmyStance.DEFENSIVE: DEF,
        ArmyStance.PACIFY: ATK_II,
        ArmyStance.RAIDING: ATK,
        ArmyStance.GUERILLA: DEF_I,
        ArmyStance.MOVING: ATK_I,
    },
    ArmyStance.DEFENSIVE: {
        ArmyStance.AGGRESSIVE: DEF,
        ArmyStance.DEFENSIVE: NEUTRAL,
        ArmyStance.PACIFY: NEUTRAL,
        ArmyStance.RAIDING: NEUTRAL,
        ArmyStance.GUERILLA: DEF,
        ArmyStance.MOVING: NEUTRAL,
    },
    ArmyStance.PACIFY: {
        ArmyStance.AGGRESSIVE: DEF_II,
        ArmyStance.DEFENSIVE: NEUTRAL,
        ArmyStance.PACIFY: NEUTRAL,
        ArmyStance.RAIDING: DEF,
        ArmyStance.GUERILLA: NEUTRAL,
        ArmyStance.MOVING: DEF_II,
    },
    ArmyStance.RAIDING: {
        ArmyStance.AGGRESSIVE: DEF,
        ArmyStance.DEFENSIVE: NEUTRAL,
        ArmyStance.PACIFY: ATK,
        ArmyStance.RAIDING: ATK,
        ArmyStance.GUERILLA: DEF,
        ArmyStance.MOVING: ATK_I,
    },
    ArmyStance.GUERILLA: {
        ArmyStance.AGGRESSIVE: ATK_I,
        ArmyStance.DEFENSIVE: ATK,
        ArmyStance.PACIFY: NEUTRAL,
        ArmyStance.RAIDING: ATK,
        ArmyStance.GUERILLA: DEF,
        ArmyStance.MOVING: ATK_II,
    },
    ArmyStance.MOVING: {
        ArmyStance.AGGRESSIVE: DEF_I,
        ArmyStance.DEFENSIVE: DEF_I,
        ArmyStance.PACIFY: NEUTRAL,
        ArmyStance.RAIDING: DEF_I,
        ArmyStance.GUERILLA: DEF_II,
        ArmyStance.MOVING: NEUTRAL,
    }
}


def stance_vs_mult(attacker: Army, defender: Army):
    atk_table = STANCE_MULT_TABLE.get(attacker.stance, None)
    if atk_table is not None:
        val = atk_table.get(defender.stance, None)
        if val is not None:
            return val
        else:
            print(f"Could not determine defender stance: {defender.stance}")
    else:
        print(f"Could not determine attacker stance: {attacker.stance}")


def atk_terrain_mult(region):
    return 1/region.terrain.defensiveness


def atk_full_mult(attacker: Army, defender: Army):
    stance_mult = stance_vs_mult(attacker, defender)
    terrain_mult = atk_terrain_mult(attacker.region)
    return stance_mult * terrain_mult


def test1(nation1, nation2):
    region = Region("test_region")
    region.terrain = Terrain.HILLS
    attacker = Army("attacker", 100, 1.0, 1.0, region, nation1, ArmyStance.AGGRESSIVE)
    defender = Army("defender", 100, 1.0, 1.0, region, nation2, ArmyStance.DEFENSIVE)
    return atk_full_mult(attacker, defender)

