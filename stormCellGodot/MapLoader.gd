extends Node2D


# Called when the node enters the scene tree for the first time.
func _ready():
	var region_color_dict=$nations.create_region_color_dict(
		$nations.read_starting_regions(),
		$nations.read_national_colors()
	)
	$regions.create_regions()
	$regions.color_regions(region_color_dict)

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
