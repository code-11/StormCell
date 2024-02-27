extends Button

signal speed_changed(new_speed)

func _pressed():
	speed_changed.emit(1)
