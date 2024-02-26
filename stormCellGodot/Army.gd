extends Polygon2D


class_name Army

var nation=null 
var stance=Constants.Stance.AGGRESSIVE 
var size=0
var quality=1 #1-100

func get_stance_as_str():
	return {
		Constants.Stance.AGGRESSIVE:"Aggressive",
		Constants.Stance.DEFENSIVE:"Defensive",
		Constants.Stance.PACIFY:"Pacify",
		Constants.Stance.RAIDING:"Raiding",
		Constants.Stance.GUERILLA:"Guerilla",
		Constants.Stance.MOVING:"Moving"
	}.get(stance,"UNDEFINED_STANCE")

func _ready():
	add_to_group("Armies")
