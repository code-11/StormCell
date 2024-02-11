extends Node


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.

func read_starting_regions():
	var starting_regions_file = FileAccess.open("res://starting_regions.json", FileAccess.READ)
	var starting_regions_data = JSON.parse_string(starting_regions_file.get_as_text())
	return starting_regions_data
	
func read_national_colors():
	var national_colors_file = FileAccess.open("res://national_colors.json", FileAccess.READ)
	var national_colors_data = JSON.parse_string(national_colors_file.get_as_text())
	return national_colors_data


func create_region_color_dict(starting_region_dict,national_colors_dict):
	var to_return={}
	for nation in starting_region_dict:
		var national_color=national_colors_dict[nation]
		var starting_regions=starting_region_dict[nation]
		for starting_region in starting_regions:
			to_return[starting_region]=national_color
	return to_return
		
		
		
	
