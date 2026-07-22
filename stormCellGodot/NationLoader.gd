extends Node

var STARTING_REGIONS_PATH="res://data/starting_regions.json"
var NATION_DATA_PATH="res://data/nation_data.json"

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.

func read_starting_regions():
	var starting_regions_file = FileAccess.open(STARTING_REGIONS_PATH, FileAccess.READ)
	var starting_regions_data = JSON.parse_string(starting_regions_file.get_as_text())
	return starting_regions_data
	
func get_region_to_starting_nation():
	var starting_nation_data = read_starting_regions()
	var to_return = {}
	for nation in starting_nation_data:
		for region_id in starting_nation_data[nation]:
			to_return[region_id] = nation
	return to_return
	
func read_nation_data():
	var nation_data_file = FileAccess.open(NATION_DATA_PATH, FileAccess.READ)
	var nation_data = JSON.parse_string(nation_data_file.get_as_text())
	return nation_data


func create_region_color_dict(starting_region_dict,nation_data_dict):
	var to_return={}
	for nation in starting_region_dict:
		var national_color=nation_data_dict[nation]["nation_color"]
		var starting_regions=starting_region_dict[nation]
		for starting_region in starting_regions:
			to_return[starting_region]=national_color
	return to_return
		
		
		
	
