extends Node

var ATK_II = 5
var ATK_I = 4
var ATK = 3
var NEUTRAL = 1  # atk needs 1:1
var DEF = .33  # atk needs 3:1
var DEF_I = .25  # atk needs 4:1
var DEF_II = .2  # atk needs 5:1

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
		SCConstants.Stance.AGGRESSIVE: DEF,
		SCConstants.Stance.DEFENSIVE: NEUTRAL,
		SCConstants.Stance.PACIFY: NEUTRAL,
		SCConstants.Stance.RAIDING: NEUTRAL,
		SCConstants.Stance.GUERILLA: DEF,
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
		

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass
