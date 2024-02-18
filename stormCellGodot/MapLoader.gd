extends Node2D

var NN_CLICK_COUNT=5
var UNOCCUPIED_REGION_COLOR="#D5CEAB"
var DEFAULT_BORDER_COLOR="#333333"
var SELECTED_BORDER_COLOR="#FF0000"

var TERRAIN_COLORS_PATH="res://data/terrain_colors.json"
#func get_clicked_region(point):
	#
	#print(Geometry2D.is_point_in_polygon(point,poly))

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
	var terrain_colors=read_terrain_color_data()
	for region in all_regions:
		to_return[region.name]=terrain_colors[region.terrain]
	return to_return
	

func read_terrain_color_data():
	var terrain_color_file = FileAccess.open(TERRAIN_COLORS_PATH, FileAccess.READ)
	var terrain_color_data = JSON.parse_string(terrain_color_file.get_as_text())
	return terrain_color_data

func _input(event):
	if event is InputEventMouseButton and event.pressed:
		if event.button_index == MOUSE_BUTTON_LEFT:
			var click_position: Vector2 = event.position
			#var ff_poly=get_node("regions/41/poly-0").polygon
			#print(Geometry2D.is_point_in_polygon(click_position,ff_poly))
			var clicked_region=$regions.get_clicked_region(click_position)
			if clicked_region!=null:
				get_parent().set_selected_region(clicked_region)


# Called when the node enters the scene tree for the first time.
func _ready():
	#var region_color_dict=$nations.create_region_color_dict(
		#$nations.read_starting_regions(),
		#$nations.read_national_colors()
	#)
	$regions.create_regions($nations.get_region_to_starting_nation())

	#$regions.color_regions(region_color_dict)
	#print(get_node("regions/41/poly-0"))

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
