extends Node2D

var player_nation = null
var PLAYER_INFO_PATH="res://data/player_info.json"

var army_uid=0

func read_player_nation():
	var player_info_file = FileAccess.open(PLAYER_INFO_PATH, FileAccess.READ)
	var player_info = JSON.parse_string(player_info_file.get_as_text())
	return player_info["nation"]

func spawn_army(nation, region):
	var army_node=Army.new()
	army_node.name="army"+str(army_uid)
	army_uid+=1
	
	army_node.nation=nation
	army_node.polygon=PackedVector2Array([
		Vector2(0,0),
		Vector2(15,0),
		Vector2(15,15),
		Vector2(0,15)
	])
	army_node.color="black"
	
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
	spawn_army("test","29")


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
