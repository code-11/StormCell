extends Node2D

var NN_CLICK_COUNT=5
var UNOCCUPIED_REGION_COLOR="#D5CEAB"
var DEFAULT_BORDER_COLOR="#333333"
var SELECTED_BORDER_COLOR="#FF0000"
var FERTILITY_NO_DATA_COLOR="#404040"

var FERTILITY_BONUS_PATH="res://data/fertility_bonus.json"

const FertilityCalc=preload("res://FertilityCalculator.gd")

enum MAP_CLICK_MODE{INFO, MOVE_ARMY}
var cur_map_click_mode=MAP_CLICK_MODE.INFO

var move_army_selected_army=null

signal move_army_msg(army,destination_region)

func set_map_click_mode_to_move_army(army):
	cur_map_click_mode=MAP_CLICK_MODE.MOVE_ARMY
	move_army_selected_army=army

func unselect_region(region):
	$regions.color_border(region,DEFAULT_BORDER_COLOR)

func set_selected_region(region):
	$regions.color_border(region,SELECTED_BORDER_COLOR)

func set_color_mode(mode):
	var region_color_dict=null
	if mode=="occupation":
		region_color_dict=create_occupation_color_dict()

	elif mode=="administration":
		region_color_dict=create_administration_color_dict()

	elif mode=="terrain":
		region_color_dict=create_terrain_color_dict()

	elif mode=="fertility":
		region_color_dict=create_fertility_color_dict()

	$regions.color_regions(region_color_dict)

func create_terrain_color_dict():
	var to_return={}
	var all_regions=$regions.get_regions()
	for region in all_regions:
		to_return[region.name]=region.terrain.color
	return to_return

func get_nation_color(nation_data,nation):
	if nation==null or not nation_data.has(nation):
		return null
	return nation_data[nation].get("nation_color",null)

func nation_strength_to_color(nation_color_hex,value):
	if nation_color_hex==null or value==null:
		return UNOCCUPIED_REGION_COLOR
	var nation_color=Color.html(nation_color_hex)
	var neutral_color=Color.html(UNOCCUPIED_REGION_COLOR)
	var alpha=clamp(value,0.0,1.0)
	var blended=neutral_color.lerp(nation_color,alpha)
	return "#"+blended.to_html(false)

func create_occupation_color_dict():
	var to_return={}
	var nation_data=$nations.read_nation_data()
	var all_regions=$regions.get_regions()
	for region in all_regions:
		var nation_color_hex=get_nation_color(nation_data,region.nation)
		to_return[region.name]=nation_strength_to_color(nation_color_hex,region.occupation)
	return to_return

func create_administration_color_dict():
	var to_return={}
	var nation_data=$nations.read_nation_data()
	var all_regions=$regions.get_regions()
	for region in all_regions:
		var nation_color_hex=get_nation_color(nation_data,region.nation)
		to_return[region.name]=nation_strength_to_color(nation_color_hex,region.administration)
	return to_return

func read_fertility_bonus():
	var fertility_file = FileAccess.open(FERTILITY_BONUS_PATH, FileAccess.READ)
	return JSON.parse_string(fertility_file.get_as_text())

func fertility_bonus_to_color(value):
	value=clamp(value,-1.0,1.0)
	var color
	if value>=0:
		color=Color(1.0-value, 1.0, 1.0-value)
	else:
		var t=-value
		color=Color(1.0, 1.0-t, 1.0-t)
	return "#"+color.to_html(false)

func create_fertility_color_dict():
	var to_return={}
	var fertility_data=read_fertility_bonus()
	var nation_data=$nations.read_nation_data()
	var all_regions=$regions.get_regions()
	for region in all_regions:
		if fertility_data.has(region.name):
			var total=FertilityCalc.calculate_region_fertility(region,fertility_data,nation_data)
			to_return[region.name]=fertility_bonus_to_color(total)
		else:
			to_return[region.name]=FERTILITY_NO_DATA_COLOR
	return to_return

func get_region_fertility_breakdown(region):
	var fertility_data=read_fertility_bonus()
	var nation_data=$nations.read_nation_data()
	return FertilityCalc.calculate_region_fertility_components(region,fertility_data,nation_data)

func _input(event):
	if event is InputEventMouseButton and event.pressed:
		if event.button_index == MOUSE_BUTTON_LEFT:
			if cur_map_click_mode== MAP_CLICK_MODE.INFO:
				var click_position: Vector2 = event.position
				#var ff_poly=get_node("regions/41/poly-0").polygon
				#print(Geometry2D.is_point_in_polygon(click_position,ff_poly))
				var clicked_region=$regions.get_clicked_region(click_position)
				if clicked_region!=null:
					get_parent().set_selected_region(clicked_region)
			elif cur_map_click_mode==MAP_CLICK_MODE.MOVE_ARMY:
				var click_position: Vector2 = event.position
				var clicked_region=$regions.get_clicked_region(click_position)
				if clicked_region!=null:
					move_army_msg.emit(move_army_selected_army,clicked_region)
					cur_map_click_mode=MAP_CLICK_MODE.INFO

func load_map():
	$regions.create_regions($nations.get_region_to_starting_data())

func attach_army(army_node,region):
	$regions.attach_army(army_node,region)
	
func get_armies(region):
	return $regions.get_armies(region)

# Called when the node enters the scene tree for the first time.
func _ready():
	pass
	#var region_color_dict=$nations.create_region_color_dict(
		#$nations.read_starting_regions(),
		#$nations.read_nation_data()
	#)
	#$regions.create_regions($nations.get_region_to_starting_nation())

	#$regions.color_regions(region_color_dict)
	#print(get_node("regions/41/poly-0"))

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
