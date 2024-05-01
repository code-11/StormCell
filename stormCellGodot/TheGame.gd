extends Node2D

var player_nation = null
var PLAYER_INFO_PATH="res://data/player_info.json"

var army_uid=0

func read_player_nation():
	var player_info_file = FileAccess.open(PLAYER_INFO_PATH, FileAccess.READ)
	var player_info = JSON.parse_string(player_info_file.get_as_text())
	return player_info["nation"]

func spawn_army(nation, region):
	var army_node=Army.new(
		"army"+str(army_uid),
		nation,
		"black",
		15
	)
	army_uid+=1
	
	$GuiCtrl.attach_army(army_node, region)

func get_armies(region):
	return $GuiCtrl.get_armies(region)

func move_army_to(army, region):
	pass

# Called when the node enters the scene tree for the first time.
func _ready():
	player_nation=read_player_nation()
	$GuiCtrl.set_player_nation(player_nation)
	$GuiCtrl.load_map()
	spawn_initial_armies()

func spawn_initial_armies():
	spawn_army("pinemar_keep","18")
	spawn_army("pinemar_keep","21")
	spawn_army("amonhold","15")
	spawn_army("northumber","76")
	spawn_army("northumber","77")
	spawn_army("seluceria","54")
	spawn_army("north_east_empire","27")
	spawn_army("north_east_empire","29")
	spawn_army("north_west_empire","10")
	spawn_army("central_empire","33")
	spawn_army("south_west_empire","26")
	spawn_army("maniabon","84")
	spawn_army("south_east_empire","39")
	spawn_army("havernia","48")
	spawn_army("naguabo","60")

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
