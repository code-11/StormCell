extends Node2D

var NN_CLICK_COUNT=5

#func get_clicked_region(point):
	#
	#print(Geometry2D.is_point_in_polygon(point,poly))

func _input(event):
	if event is InputEventMouseButton and event.pressed:
		if event.button_index == MOUSE_BUTTON_LEFT:
			var click_position: Vector2 = event.position
			#var ff_poly=get_node("regions/41/poly-0").polygon
			#print(Geometry2D.is_point_in_polygon(click_position,ff_poly))
			var clicked_region=$regions.get_clicked_region(click_position)
			$regions.color_border(clicked_region,"#FF0000")


# Called when the node enters the scene tree for the first time.
func _ready():
	var region_color_dict=$nations.create_region_color_dict(
		$nations.read_starting_regions(),
		$nations.read_national_colors()
	)
	$regions.create_regions()
	$regions.color_regions(region_color_dict)
	#print(get_node("regions/41/poly-0"))

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
