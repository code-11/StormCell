extends Button

signal set_speed_play_2

func _pressed():
	set_speed_play_2.emit()
