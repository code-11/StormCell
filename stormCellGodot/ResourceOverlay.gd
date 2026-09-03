extends Node2D

const RESOURCE_DATA_PATH = "res://data/resource_data.json"
const REGION_RESOURCES_PATH = "res://data/region_resources.json"
const SQUARE_SIZE = 6.0
const SQUARE_SPACING = 8.0
const SQUARES_PER_ROW = 3

var resource_data = null
var region_resources = null

func _ready():
	resource_data = SCConstants.load_json_file(RESOURCE_DATA_PATH)
	region_resources = SCConstants.load_json_file(REGION_RESOURCES_PATH)

func _draw():
	var geo = get_parent()
	var gui = get_node_or_null("/root/Node2D/TheGame/GuiCtrl")
	if gui == null or gui.map_color_mode != "resources":
		return
	for region in geo.get_regions():
		var resources_here = region_resources.get(region.name, {})
		if resources_here.is_empty():
			continue
		var resource_names = resources_here.keys()
		resource_names.sort()
		var center = geo.get_bb_center(geo.get_region_bb(region))
		var origin = Vector2(center[0], center[1])
		for i in range(resource_names.size()):
			var color_hex = resource_data.get(resource_names[i], {}).get("color", "#ffffff")
			var col = i % SQUARES_PER_ROW
			var row = i / SQUARES_PER_ROW
			var offset = Vector2(
				(col - (SQUARES_PER_ROW - 1) / 2.0) * SQUARE_SPACING,
				row * SQUARE_SPACING
			)
			var top_left = origin + offset - Vector2(SQUARE_SIZE, SQUARE_SIZE) / 2.0
			draw_rect(Rect2(top_left, Vector2(SQUARE_SIZE, SQUARE_SIZE)), Color.html(color_hex))

func _process(_delta):
	queue_redraw()
