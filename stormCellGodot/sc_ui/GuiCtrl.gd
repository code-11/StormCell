extends Node

var selected_region=null
var map_mode="pol"

func set_selected_region(region):
	#reset previous selected region's border color
	if selected_region!=null:
		$TheMap.unselect_region(selected_region)
	
	selected_region = region
	$TheMap.set_selected_region(region)
	$ThePanel.set_selected_region(region)

func set_map_mode(new_mode):
	map_mode=new_mode
	$TheMap.set_color_mode(new_mode)


func _ready():
	set_map_mode(map_mode)
