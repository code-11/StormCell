extends Polygon2D


class_name Army

var nation=null
var stance=SCConstants.Stance.AGGRESSIVE
var size=50 #1-99
var quality=1 #1-99
var stance_lock=null #Null for no lock, or Days as a number, after passed, can change stance.
var in_battle=false

var visual_half=7.5

var size_lbl=Label.new()
var battle_chip=Polygon2D.new()

func handle_stance_unlock(cur_days):
	if stance_lock and stance_lock < cur_days:
		stance_lock=null

func can_change_stance():
	return stance_lock==null

func get_stance_as_str():
	return {
		SCConstants.Stance.AGGRESSIVE:"Aggressive",
		SCConstants.Stance.DEFENSIVE:"Defensive",
		SCConstants.Stance.PACIFY:"Pacify",
		SCConstants.Stance.RAIDING:"Raiding",
		SCConstants.Stance.GUERILLA:"Guerilla",
		SCConstants.Stance.MOVING:"Moving"
	}.get(stance,"UNDEFINED_STANCE")


func _init(name, nation, color, size):
	self.name=name
	self.nation=nation
	self.color=Color.html(color)
	var half=size/2.0
	visual_half=half
	self.polygon=PackedVector2Array([
		Vector2(-half,-half),
		Vector2(half,-half),
		Vector2(half,half),
		Vector2(-half,half)
	])

func set_in_battle(val):
	in_battle=val
	battle_chip.visible=val

func _ready():
	add_to_group(SCConstants.ARMY_GROUP)

	# Label centered within the token bounds
	size_lbl.z_index=1
	size_lbl.set("theme_override_font_sizes/font_size", 10)
	size_lbl.position=Vector2(-visual_half, -visual_half)
	size_lbl.size=Vector2(visual_half*2, visual_half*2)
	size_lbl.horizontal_alignment=HORIZONTAL_ALIGNMENT_CENTER
	size_lbl.vertical_alignment=VERTICAL_ALIGNMENT_CENTER
	add_child(size_lbl)

	# Black outline drawn on top of the filled polygon
	var outline=Line2D.new()
	outline.default_color=Color.BLACK
	outline.width=2.0
	outline.points=PackedVector2Array([
		Vector2(-visual_half,-visual_half),
		Vector2(visual_half,-visual_half),
		Vector2(visual_half,visual_half),
		Vector2(-visual_half,visual_half),
		Vector2(-visual_half,-visual_half)
	])
	outline.z_index=1
	add_child(outline)

	# Battle chip: small red square at top-right corner
	var chip_half=4.0
	battle_chip.color=Color.RED
	battle_chip.polygon=PackedVector2Array([
		Vector2(-chip_half,-chip_half),
		Vector2(chip_half,-chip_half),
		Vector2(chip_half,chip_half),
		Vector2(-chip_half,chip_half)
	])
	battle_chip.position=Vector2(visual_half+chip_half, -(visual_half+chip_half))
	battle_chip.z_index=2
	battle_chip.visible=false
	add_child(battle_chip)

func _process(delta):
	self.size_lbl.text=str(int(self.size))

func _to_string():
	return "<Army "+self.name+","+self.nation+","+get_stance_as_str()+","+str(self.size)+">"
