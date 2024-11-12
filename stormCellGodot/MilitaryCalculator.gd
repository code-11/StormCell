extends Node

const ATK_II = 5
const ATK_I = 4
const ATK = 3
const NEUTRAL = 1  # atk needs 1:1
const DEF = .33  # atk needs 3:1
const DEF_I = .25  # atk needs 4:1
const DEF_II = .2  # atk needs 5:1

const BASE_DISCOVER_CHANCE =.05 #Given two armies w/ no other modifiers, find each other average within 20 ticks

# Outer layer is attacker
var STANCE_MULT_TABLE = {
	SCConstants.Stance.AGGRESSIVE: {
		SCConstants.Stance.AGGRESSIVE: NEUTRAL,
		SCConstants.Stance.DEFENSIVE: DEF,
		SCConstants.Stance.PACIFY: ATK_II,
		SCConstants.Stance.RAIDING: ATK,
		SCConstants.Stance.GUERILLA: DEF_I,
		SCConstants.Stance.MOVING: ATK_I,
	},
	SCConstants.Stance.DEFENSIVE: {
		SCConstants.Stance.AGGRESSIVE: NEUTRAL,
		SCConstants.Stance.DEFENSIVE: NEUTRAL,
		SCConstants.Stance.PACIFY: NEUTRAL,
		SCConstants.Stance.RAIDING: DEF,
		SCConstants.Stance.GUERILLA: NEUTRAL,
		SCConstants.Stance.MOVING: NEUTRAL,
	},
	SCConstants.Stance.PACIFY: {
		SCConstants.Stance.AGGRESSIVE: DEF_II,
		SCConstants.Stance.DEFENSIVE: NEUTRAL,
		SCConstants.Stance.PACIFY: NEUTRAL,
		SCConstants.Stance.RAIDING: DEF,
		SCConstants.Stance.GUERILLA: NEUTRAL,
		SCConstants.Stance.MOVING: DEF_II,
	},
	SCConstants.Stance.RAIDING: {
		SCConstants.Stance.AGGRESSIVE: DEF,
		SCConstants.Stance.DEFENSIVE: NEUTRAL,
		SCConstants.Stance.PACIFY: ATK,
		SCConstants.Stance.RAIDING: ATK,
		SCConstants.Stance.GUERILLA: DEF,
		SCConstants.Stance.MOVING: ATK_I,
	},
	SCConstants.Stance.GUERILLA: {
		SCConstants.Stance.AGGRESSIVE: ATK_I,
		SCConstants.Stance.DEFENSIVE: ATK,
		SCConstants.Stance.PACIFY: NEUTRAL,
		SCConstants.Stance.RAIDING: ATK,
		SCConstants.Stance.GUERILLA: DEF,
		SCConstants.Stance.MOVING: ATK_II,
	},
	SCConstants.Stance.MOVING: {
		SCConstants.Stance.AGGRESSIVE: DEF_I,
		SCConstants.Stance.DEFENSIVE: DEF_I,
		SCConstants.Stance.PACIFY: NEUTRAL,
		SCConstants.Stance.RAIDING: DEF_I,
		SCConstants.Stance.GUERILLA: DEF_II,
		SCConstants.Stance.MOVING: NEUTRAL,
	}
}

func calculate_stance_multiplier(attacker:Army, defender:Army):
		return STANCE_MULT_TABLE[attacker.stance][defender.stance]
		
func calculate_terrain_multiplier(region):
	var defensiveness = region.terrain.defensiveness
	var mult=1/float(defensiveness)
	return mult

func calculate_full_multiplier(attacker: Army, defender: Army, region):
	var stance_mult = calculate_stance_multiplier(attacker, defender)
	var terrain_mult = calculate_terrain_multiplier(region)
	return stance_mult * terrain_mult

func calculate_discover_multiplier(attacker: Army, defender: Army, region):
	#TODO: Make it vary on stance
	return (1/float(region.terrain.defensiveness)) * BASE_DISCOVER_CHANCE

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass
