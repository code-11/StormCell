extends Button

class_name StanceButton

var stance=null

func _init(a_stance,a_button_group,min_size,icon_path):
	stance=a_stance
	button_group=a_button_group
	custom_minimum_size=min_size
	icon=load(icon_path)
	expand_icon=true
	size_flags_horizontal=Control.SIZE_SHRINK_BEGIN
	toggle_mode=true
