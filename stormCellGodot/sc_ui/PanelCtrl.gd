extends PanelContainer

func get_region_label():
	return get_node("VBoxContainer/RegionInfoBox/RegionDisplayLbl")

func get_terrain_label():
	return get_node("VBoxContainer/RegionInfoBox/TerrainTypeLbl")

func get_nation_label():
	return get_node("VBoxContainer/RegionInfoBox/NationOwnerLbl")

func get_fertility_label():
	return get_node("VBoxContainer/RegionInfoBox/FertilityLbl")

func get_occupation_label():
	return get_node("VBoxContainer/RegionInfoBox/OccupationLbl")

func get_administration_label():
	return get_node("VBoxContainer/RegionInfoBox/AdministrationLbl")

func get_resources_label():
	return get_node("VBoxContainer/RegionInfoBox/ResourcesLbl")

func get_player_nation_label():
	return get_node("VBoxContainer/HBoxContainer/VBoxContainer/PlayerNationLbl")

func get_army_info_ctrl():
	return get_node("VBoxContainer/RegionInfoBox/ArmyInfoBox")

func set_player_nation(player_nation):
	var player_nation_lbl = get_player_nation_label()
	player_nation_lbl.text=player_nation

func set_selected_region(region, fertility_breakdown, resource_breakdown):
	var region_lbl=get_region_label()
	region_lbl.text="Name: "+region.name

	var terrain_lbl=get_terrain_label()
	terrain_lbl.text="Terrain: "+region.terrain.name

	var nation_lbl = get_nation_label()
	nation_lbl.text="Nation: "+str(region.nation)

	var fertility_lbl=get_fertility_label()
	fertility_lbl.text=format_fertility_breakdown(fertility_breakdown)

	var occupation_lbl=get_occupation_label()
	occupation_lbl.text="Occupation: "+format_value_or_na(region.occupation)

	var administration_lbl=get_administration_label()
	administration_lbl.text="Administration: "+format_value_or_na(region.administration)

	var resources_lbl=get_resources_label()
	resources_lbl.text=format_resource_breakdown(resource_breakdown)

func format_fertility_breakdown(fertility_breakdown):
	var region_bonus_text = ("%.2f" % fertility_breakdown.region_bonus) if fertility_breakdown.has_region_data else "N/A"
	return "Fertility: %.2f\n  Region: %s\n  Terrain: %.2f\n  National: %.2f" % [
		fertility_breakdown.total,
		region_bonus_text,
		fertility_breakdown.terrain_bonus,
		fertility_breakdown.national_bonus,
	]

func format_resource_breakdown(resource_breakdown):
	if resource_breakdown.is_empty():
		return "Resources: None"
	var lines=["Resources:"]
	for resource_name in resource_breakdown:
		var components=resource_breakdown[resource_name]
		lines.append("  %s: %.2f (abundance %.2f x ease %.2f)" % [
			resource_name.capitalize(),
			components.total,
			components.abundance,
			components.ease,
		])
	return "\n".join(lines)

func format_value_or_na(value):
	return ("%.2f" % value) if value != null else "N/A"

func set_armies(armies):
	var army_info_box=get_army_info_ctrl()
	for army in armies:
		army_info_box.add_army(army)

func reset_armies():
	var army_info_box=get_army_info_ctrl()
	army_info_box.reset_armies()
