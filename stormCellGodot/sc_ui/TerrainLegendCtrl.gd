extends PanelContainer

class_name TerrainLegendCtrl

const TERRAIN_DATA_PATH = "res://data/terrain_data.json"
const SWATCH_SIZE = Vector2(14, 14)

func _ready():
	visible = false
	_build_legend()

func _build_legend():
	var terrain_data = SCConstants.load_json_file(TERRAIN_DATA_PATH)
	var vbox = VBoxContainer.new()
	add_child(vbox)

	var title = Label.new()
	title.text = "Terrain"
	vbox.add_child(title)

	var terrain_names = terrain_data.keys()
	terrain_names.sort()
	for terrain_name in terrain_names:
		var row = HBoxContainer.new()
		vbox.add_child(row)

		var swatch = ColorRect.new()
		swatch.color = Color.html(terrain_data[terrain_name].get("color", "#ffffff"))
		swatch.custom_minimum_size = SWATCH_SIZE
		row.add_child(swatch)

		var label = Label.new()
		label.text = " " + terrain_name.capitalize()
		row.add_child(label)
