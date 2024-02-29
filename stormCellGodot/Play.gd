extends Button

signal set_speed_play

func _pressed():
	set_speed_play.emit()
