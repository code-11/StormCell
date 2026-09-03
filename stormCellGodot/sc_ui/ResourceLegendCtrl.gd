extends PanelContainer

class_name ResourceLegendCtrl

const RESOURCE_DATA_PATH = "res://data/resource_data.json"
const SWATCH_SIZE = Vector2(14, 14)

func _ready():
	visible = false
	_build_legend()

func _build_legend():
	var resource_data = SCConstants.load_json_file(RESOURCE_DATA_PATH)
	var vbox = VBoxContainer.new()
	add_child(vbox)

	var title = Label.new()
	title.text = "Resources"
	vbox.add_child(title)

	var resource_names = resource_data.keys()
	resource_names.sort()
	for resource_name in resource_names:
		var row = HBoxContainer.new()
		vbox.add_child(row)

		var swatch = ColorRect.new()
		swatch.color = Color.html(resource_data[resource_name].get("color", "#ffffff"))
		swatch.custom_minimum_size = SWATCH_SIZE
		row.add_child(swatch)

		var label = Label.new()
		label.text = " " + resource_name.capitalize()
		row.add_child(label)
