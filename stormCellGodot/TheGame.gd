extends Node2D

var player_nation = null
var PLAYER_INFO_PATH="res://data/player_info.json"

func read_player_nation():
	var player_info_file = FileAccess.open(PLAYER_INFO_PATH, FileAccess.READ)
	var player_info = JSON.parse_string(player_info_file.get_as_text())
	return player_info["nation"]

# Called when the node enters the scene tree for the first time.
func _ready():
	player_nation=read_player_nation()
	$GuiCtrl.set_player_nation(player_nation)
	$GuiCtrl.load_map()


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
