extends Polygon2D

class_name Army

enum {AGGRESSIVE,DEFENSIVE,PACIFY,RAIDING,GUERILLA,MOVING}

var nation=null 
var stance=AGGRESSIVE 

func _ready():
	add_to_group("Armies")
