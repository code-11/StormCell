extends Node

class_name GoodsCalculator

"""
This file dispatches a good to whichever yield source it's defined with — fertility
(crops, cash crops) or abundance (minerals, quarried/mined goods) — and returns a
breakdown in the same shape regardless of source, so callers (UI, production) don't
need to care which kind of good they're looking at.

Fertility-sourced goods reuse FertilityCalculator's output rather than recomputing
region/terrain/national bonuses a second time.
"""

const FertilityCalc = preload("res://FertilityCalculator.gd")
const ResourceCalc = preload("res://ResourceCalculator.gd")

static func calculate_region_good_components(region, good_name, resource_data_dict, region_resource_dict, region_fertility_dict, nation_data_dict):
	var good_def = resource_data_dict.get(good_name, {})
	var yield_source = good_def.get("yield_source", "abundance")
	if yield_source == "fertility":
		return _calculate_fertility_good(region, good_def, region_fertility_dict, nation_data_dict)
	return ResourceCalc.calculate_region_resource_components(region, good_name, region_resource_dict, resource_data_dict, nation_data_dict)

static func _calculate_fertility_good(region, good_def, region_fertility_dict, nation_data_dict):
	var fertility_components = FertilityCalc.calculate_region_fertility_components(region, region_fertility_dict, nation_data_dict)
	var suitable_terrain = good_def.get("suitable_terrain", null)
	var is_suitable = suitable_terrain == null or (region.terrain != null and suitable_terrain.has(region.terrain.name))
	var multiplier = good_def.get("fertility_multiplier", 1.0)
	var total = (fertility_components.total * multiplier) if is_suitable else 0.0
	return {
		"has_region_data": fertility_components.has_region_data,
		"fertility": fertility_components.total,
		"is_suitable": is_suitable,
		"multiplier": multiplier,
		"total": total,
	}

static func calculate_region_good(region, good_name, resource_data_dict, region_resource_dict, region_fertility_dict, nation_data_dict):
	return calculate_region_good_components(region, good_name, resource_data_dict, region_resource_dict, region_fertility_dict, nation_data_dict).total
