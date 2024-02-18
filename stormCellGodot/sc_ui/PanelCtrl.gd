extends PanelContainer

func get_region_label():
	return get_node("VBoxContainer/RegionInfoBox/RegionDisplayLbl")

func get_terrain_label():
	return get_node("VBoxContainer/RegionInfoBox/TerrainTypeLbl")

func get_nation_label():
	return get_node("VBoxContainer/RegionInfoBox/NationOwnerLbl")

func get_player_nation_label():
	return get_node("VBoxContainer/HBoxContainer/VBoxContainer/PlayerNationLbl")

func set_player_nation(player_nation):
	var player_nation_lbl = get_player_nation_label()
	player_nation_lbl.text=player_nation

func set_selected_region(region):
	var region_lbl=get_region_label()
	region_lbl.text="Name: "+region.name
	
	var terrain_lbl=get_terrain_label()
	terrain_lbl.text="Terrain: "+region.terrain
	
	var nation_lbl = get_nation_label()
	nation_lbl.text="Nation: "+str(region.nation)
