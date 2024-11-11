extends Node

class_name Terrain

var color="white"
var defensiveness=0 # multiplier
var mobility = 0 # multiplier
var attrition = 0 # multiplier

static func from_json_dict(name,json_dict):
	return Terrain.new(
		name,
		json_dict["color"],
		json_dict["defensiveness"],
		json_dict["mobility"],
		json_dict["attrition"]
	)

func _init(name, color, defensiveness, mobility, attrition):
	self.name=name
	self.color=color
	self.defensiveness=defensiveness
	self.mobility=mobility
	self.attrition=attrition
