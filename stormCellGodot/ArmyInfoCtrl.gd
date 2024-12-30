extends VBoxContainer

var cur_armies=[]
var cur_army_items=[]

func _handle_army_gui_item_stance_change_attempt(army,new_stance,stance_lbl):
	print("Got: ",army,new_stance,stance_lbl)

func add_army(army):
	cur_armies.append(army)
	
	var army_item= ArmyGuiItem.new(army)
	add_child(army_item)
	self.connect("army_gui_item_stance_change_attempt",_handle_army_gui_item_stance_change_attempt)
	
	cur_army_items.append(army_item)

func reset_armies():
	for army_item in cur_army_items: 
		remove_child(army_item)
	cur_armies.clear()
	cur_army_items.clear()

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
