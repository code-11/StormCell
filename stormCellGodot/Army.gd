extends Polygon2D


class_name Army

var nation=null 
var stance=SCConstants.Stance.AGGRESSIVE 
var size=0
var quality=1 #1-100

func get_stance_as_str():
	return {
		SCConstants.Stance.AGGRESSIVE:"Aggressive",
		SCConstants.Stance.DEFENSIVE:"Defensive",
		SCConstants.Stance.PACIFY:"Pacify",
		SCConstants.Stance.RAIDING:"Raiding",
		SCConstants.Stance.GUERILLA:"Guerilla",
		SCConstants.Stance.MOVING:"Moving"
	}.get(stance,"UNDEFINED_STANCE")

func _ready():
	add_to_group("Armies")
