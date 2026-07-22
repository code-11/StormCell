extends Node

class_name FertilityCalculator

"""
This file is a helper which should contain all the non-game state related fertility calculations.
This should not look up anything in the game state tree and should only have static functions
"""

static func calculate_region_fertility_components(region, region_bonus_dict, nation_data_dict):
	var has_region_data = region_bonus_dict.has(region.name)
	var region_bonus = region_bonus_dict.get(region.name, 0.0)
	var terrain_bonus = region.terrain.fertility if region.terrain != null else 0.0
	var national_bonus = 0.0
	if region.nation != null and nation_data_dict.has(region.nation):
		national_bonus = nation_data_dict[region.nation].get("fertility_bonus", 0.0)
	return {
		"has_region_data": has_region_data,
		"region_bonus": region_bonus,
		"terrain_bonus": terrain_bonus,
		"national_bonus": national_bonus,
		"total": region_bonus + terrain_bonus + national_bonus,
	}

static func calculate_region_fertility(region, region_bonus_dict, nation_data_dict):
	return calculate_region_fertility_components(region, region_bonus_dict, nation_data_dict).total
