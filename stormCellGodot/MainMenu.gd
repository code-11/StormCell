extends VBoxContainer


func _ready():
	# Get the screen width
	var screen_width = get_window().get_size().x
	var screen_height = get_window().get_size().y

	# Set the VBoxContainer width to the screen width
	size.x = screen_width/3
	position.x = screen_width/3

	position.y = screen_height/4
