extends Node

class_name  MilitaryCalculator

"""
This file is a helper which should contain all the non-game state related military calculations.
This should not look up anything in the game state tree and should only have static functions
"""

const ATK_II = 5
const ATK_I = 4
const ATK = 3
const NEUTRAL = 1  # atk needs 1:1
const DEF = .33  # atk needs 3:1
const DEF_I = .25  # atk needs 4:1
const DEF_II = .2  # atk needs 5:1

const BASE_DISCOVER_CHANCE =.05 #Given two armies w/ no other modifiers, find each other average within 20 ticks

static var ATTACKYNESS_TABLE = {
	SCConstants.Stance.AGGRESSIVE:1,
	SCConstants.Stance.RAIDING:2,
	SCConstants.Stance.MOVING:3,
	SCConstants.Stance.GUERILLA:4,
	SCConstants.Stance.PACIFY:5,
	SCConstants.Stance.DEFENSIVE:6,
}

# Outer layer is attacker
static var STANCE_MULT_TABLE = {
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

static func calculate_stance_multiplier(attacker:Army, defender:Army):
		return STANCE_MULT_TABLE[attacker.stance][defender.stance]
		
static func calculate_terrain_multiplier(region):
	var defensiveness = region.terrain.defensiveness
	var mult=1/float(defensiveness)
	return mult

static func calculate_full_multiplier(attacker: Army, defender: Army, region):
	var stance_mult = calculate_stance_multiplier(attacker, defender)
	var terrain_mult = calculate_terrain_multiplier(region)
	return stance_mult * terrain_mult

static func calculate_discover_multiplier(attacker: Army, defender: Army, region):
	#TODO: Make it vary on stance
	return (1/float(region.terrain.defensiveness)) * BASE_DISCOVER_CHANCE

static func determine_attacker(region, army1, army2):
	#First check stance
	var army1_attky= ATTACKYNESS_TABLE[army1.stance]
	var army2_attky= ATTACKYNESS_TABLE[army2.stance]
	if army1_attky<army2_attky:
		return [army1,army2]
	elif army2_attky<army1_attky:
		return [army2,army1]
	else:
	#On a tie, defer to Dejure control 
		if army1.nation==region.nation:
			return [army1,army2]
		elif army2.nation==region.nation:
			return [army2,army1]
		#TODO: If neither involved, defer to defacto control
		#SKIPPED FOR NOW
		#TODO: Break further ties by how long the army has been on the tile
		else:
			#Final break, just string compare nations
			if army1.nation > army2.nation:
				return [army1,army2]
			else:
				return [army2,army1]
		

func calculate_one_day_battle(attacker: Army, defender: Army, region):
	pass
	

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass
