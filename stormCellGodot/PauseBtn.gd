extends Button

signal set_speed_paused

func _pressed():
	set_speed_paused.emit()
