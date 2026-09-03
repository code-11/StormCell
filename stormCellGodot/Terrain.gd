extends Node

class_name Terrain

var color="white"
var defensiveness=0 # multiplier
var mobility = 0 # multiplier
var attrition = 0 # multiplier
var fertility = 0 # bonus
var resource_ease = {} # per-resource ease-of-extraction bonus

static func from_json_dict(name,json_dict):
	return Terrain.new(
		name,
		json_dict["color"],
		json_dict["defensiveness"],
		json_dict["mobility"],
		json_dict["attrition"],
		json_dict.get("fertility", 0),
		json_dict.get("resource_ease", {})
	)

func _init(name, color, defensiveness, mobility, attrition, fertility=0, resource_ease={}):
	self.name=name
	self.color=color
	self.defensiveness=defensiveness
	self.mobility=mobility
	self.attrition=attrition
	self.fertility=fertility
	self.resource_ease=resource_ease
