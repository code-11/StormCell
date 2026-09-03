extends Node

class_name ResourceCalculator

"""
This file is a helper which should contain all the non-game state related resource
abundance/extraction calculations. This should not look up anything in the game state
tree and should only have static functions.
"""

static func calculate_region_resource_components(region, resource_name, region_resource_dict, resource_data_dict, nation_data_dict):
	var region_data = region_resource_dict.get(region.name, {})
	var has_region_data = region_data.has(resource_name)
	var abundance = region_data.get(resource_name, 0.0)
	var resource_def = resource_data_dict.get(resource_name, {})
	var base_ease = resource_def.get("base_ease", 0.0)
	var terrain_ease = 0.0
	if region.terrain != null:
		terrain_ease = region.terrain.resource_ease.get(resource_name, 0.0)
	var tech_ease = 0.0
	if region.nation != null and nation_data_dict.has(region.nation):
		var nation_tech_ease = nation_data_dict[region.nation].get("resource_tech_ease", {})
		tech_ease = nation_tech_ease.get(resource_name, 0.0)
	var ease = base_ease + terrain_ease + tech_ease
	return {
		"has_region_data": has_region_data,
		"abundance": abundance,
		"base_ease": base_ease,
		"terrain_ease": terrain_ease,
		"tech_ease": tech_ease,
		"ease": ease,
		"total": abundance * ease,
	}

static func calculate_region_resource(region, resource_name, region_resource_dict, resource_data_dict, nation_data_dict):
	return calculate_region_resource_components(region, resource_name, region_resource_dict, resource_data_dict, nation_data_dict).total
