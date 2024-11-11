extends Node2D

var NN_CLICK_COUNT=5
var UNOCCUPIED_REGION_COLOR="#D5CEAB"
var DEFAULT_BORDER_COLOR="#333333"
var SELECTED_BORDER_COLOR="#FF0000"

enum MAP_CLICK_MODE{INFO, MOVE_ARMY}
var cur_map_click_mode=MAP_CLICK_MODE.INFO

var move_army_selected_army=null


func set_map_click_mode_to_move_army(army):
	cur_map_click_mode=MAP_CLICK_MODE.MOVE_ARMY
	move_army_selected_army=army

func unselect_region(region):
	$regions.color_border(region,DEFAULT_BORDER_COLOR)

func set_selected_region(region):
	$regions.color_border(region,SELECTED_BORDER_COLOR)

func set_color_mode(mode):
	var region_color_dict=null
	if mode=="pol":
		region_color_dict=$nations.create_region_color_dict(
			$nations.read_starting_regions(),
			$nations.read_national_colors()
		)
	
	elif mode=="terrain": 
		region_color_dict=create_terrain_color_dict()
	
	$regions.color_regions(region_color_dict)

func create_terrain_color_dict():
	var to_return={}
	var all_regions=$regions.get_children()
	for region in all_regions:
		to_return[region.name]=region.terrain.color
	return to_return

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
					#TODO Also set army as locked for a bit
					$regions.move_army(move_army_selected_army,clicked_region)
					cur_map_click_mode=MAP_CLICK_MODE.INFO

func load_map():
	$regions.create_regions($nations.get_region_to_starting_nation())

func attach_army(army_node,region):
	$regions.attach_army(army_node,region)
	
func get_armies(region):
	return $regions.get_armies(region)

# Called when the node enters the scene tree for the first time.
func _ready():
	pass
	#var region_color_dict=$nations.create_region_color_dict(
		#$nations.read_starting_regions(),
		#$nations.read_national_colors()
	#)
	#$regions.create_regions($nations.get_region_to_starting_nation())

	#$regions.color_regions(region_color_dict)
	#print(get_node("regions/41/poly-0"))

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
