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

func get_region_to_starting_data():
	var starting_nation_data = read_starting_regions()
	var to_return = {}
	for nation in starting_nation_data:
		for region_id in starting_nation_data[nation]:
			var region_values = starting_nation_data[nation][region_id]
			to_return[region_id] = {
				"nation": nation,
				"occupation": region_values.get("occupation", null),
				"administration": region_values.get("administration", null)
			}
	return to_return

func read_nation_data():
	var nation_data_file = FileAccess.open(NATION_DATA_PATH, FileAccess.READ)
	var nation_data = JSON.parse_string(nation_data_file.get_as_text())
	return nation_data

