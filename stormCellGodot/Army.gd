extends Polygon2D


class_name Army

var nation=null 
var stance=SCConstants.Stance.AGGRESSIVE 
var size=50 #1-99
var quality=1 #1-99
var stance_lock=null #Null for no lock, or Days as a number, after passed, can change stance.

var size_lbl=Label.new()

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
	self.color=color
	self.polygon=PackedVector2Array([
		Vector2(0,0),
		Vector2(size,0),
		Vector2(size,size),
		Vector2(0,size)
	])

func _ready():
	self.add_child(size_lbl)
	size_lbl.z_index=1
	size_lbl.set("theme_override_font_sizes/font_size", 10)
	add_to_group(SCConstants.ARMY_GROUP)

func _process(delta):
	self.size_lbl.text=str(int(self.size))
	
func _to_string():	
	return "<Army "+self.name+","+self.nation+","+get_stance_as_str()+","+str(self.size)+">"
