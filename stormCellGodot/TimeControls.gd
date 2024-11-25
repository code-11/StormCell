extends HBoxContainer

signal speed_changed(new_value)

var cumulative_time=0
var PAUSE_MULTIPLIER=0
var PLAY_MULTIPLIER=1.0/2000
var PLAY_2_MULTIPLIER=1.0/1000
var PLAY_3_MULTIPLIER=2.0/1000

var cur_time_multiplier=PAUSE_MULTIPLIER

var	last_time=0	
var last_tup=[0,0,0]
	
func _on_speed_set_pause():
	cur_time_multiplier=PAUSE_MULTIPLIER
	
func _on_speed_set_play():
	cur_time_multiplier=PLAY_MULTIPLIER
	
func _on_speed_set_play_2():
	cur_time_multiplier=PLAY_2_MULTIPLIER
	
func _on_speed_set_play_3():
	cur_time_multiplier=PLAY_3_MULTIPLIER
	

func days_to_tup(input_days):
	var years = floor(input_days / 400.0)
	var remaining_days = int(input_days) % 400

	var months = floor(remaining_days / 30.0)
	remaining_days = int(remaining_days) % 30

	var days = remaining_days
	return [years, months, days]

func update_lbl(time_tup):
	$Label.text=str(time_tup[0])+":"+str(time_tup[1])+":"+str(time_tup[2])

func _process(delta):
	#TODO This sucks, optimize it.
	var cur_time=Time.get_ticks_msec()
	var diff = (cur_time-last_time) * cur_time_multiplier	
	cumulative_time += diff
	var cur_tup=days_to_tup(cumulative_time)
	if cur_tup!=last_tup:
		update_lbl(cur_tup)
		every_day()
	last_time = cur_time
	last_tup=cur_tup
	
	
func check_and_initiate_battle():
	var regions=get_node("/root/Node2D/TheGame/GuiCtrl/TheMap/regions")
	var region_armies_multimap = regions.get_armies_and_their_regions()
	var possible_battle_init_func = Callable(regions, "possible_battle_init")
	region_armies_multimap.map(possible_battle_init_func)
		
	
func every_day():
	check_and_initiate_battle()
	print("Day!")
				
func _ready():
	$Pause.set_speed_paused.connect(_on_speed_set_pause)
	$Play.set_speed_play.connect(_on_speed_set_play)
	$Play_2.set_speed_play_2.connect(_on_speed_set_play_2)
	$Play_3.set_speed_play_3.connect(_on_speed_set_play_3)
	$Pause.button_pressed=true
	$Pause.grab_focus()
