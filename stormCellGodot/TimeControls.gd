extends HBoxContainer

signal speed_changed(new_value)

var starting_time=0
var time_multiplier=1000
var cur_time_multiplier=1000 #How many miliseconds in a decimal hour
var last_day = starting_time / cur_time_multiplier

var cur_day=0
var cur_month=9
var cur_year=1020
	
func _on_speed_changed(new_speed):
	cur_time_multiplier=time_multiplier*new_speed

func days_to_tup(input_days):
	var years = floor(input_days / 400)
	var remaining_days = input_days % 400

	var months = floor(remaining_days / 30)
	remaining_days = remaining_days % 30

	var days = remaining_days
	return [years, months, days]

func _process(delta):
	var raw_day = (Time.get_ticks_msec()-starting_time) / cur_time_multiplier
	if raw_day > last_day:
		print(days_to_tup(raw_day))
		last_day = raw_day
				
func _ready():
	speed_changed.connect(_on_speed_changed)

	
		


func _on_pause_speed_changed(new_speed):
	pass # Replace with function body.
