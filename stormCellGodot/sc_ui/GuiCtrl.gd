extends Node

var selected_region=null
var map_color_mode="pol" # Or "terrain" 


func set_selected_region(region):
	#reset previous selected region's border color
	if selected_region!=null:
		$TheMap.unselect_region(selected_region)
		$ThePanel.reset_armies()
	
	selected_region = region
	$TheMap.set_selected_region(region)
	$ThePanel.set_selected_region(region)
	
	var armies = $TheMap.get_armies(region)
	$ThePanel.set_armies(armies)

func set_map_color_mode(new_mode):
	map_color_mode=new_mode
	$TheMap.set_color_mode(new_mode)

func set_player_nation(player_nation):
	$ThePanel.set_player_nation(player_nation)

func attach_army(army_node,region):
	$TheMap.attach_army(army_node,region)

func get_armies(region):
	return $TheMap.get_armies(region)

func load_map():
	$TheMap.load_map()
	set_map_color_mode("pol")
