extends VBoxContainer

var cur_armies=[]
var cur_army_lbls=[]

func add_army(army):
	cur_armies.append(army)
	
	var army_lbl=Label.new()
	army_lbl.text=army.name
	add_child(army_lbl)
	
	cur_army_lbls.append(army_lbl)

func reset_armies():
	for army_lbl in cur_army_lbls: 
		remove_child(army_lbl)
	cur_armies.clear()
	cur_army_lbls.clear()

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
