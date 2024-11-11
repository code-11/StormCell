extends Button

func get_gui_ctrl():
	return get_parent().get_parent().get_parent()

func _pressed():
	get_gui_ctrl().set_map_color_mode("terrain")
