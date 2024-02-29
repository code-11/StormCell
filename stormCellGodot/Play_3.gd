extends Button

signal set_speed_play_3

func _pressed():
	set_speed_play_3.emit()
