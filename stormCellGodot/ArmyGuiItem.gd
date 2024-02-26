extends VBoxContainer

class_name ArmyGuiItem

var the_army=null
var name_lbl=null
var nation_lbl=null
var size_lbl=null
var quality_lbl=null
var stance_lbl=null
var actions_box=null

func set_army_stance(army,stance,lbl):
	army.stance=stance
	lbl.text=the_army.get_stance_as_str()

func _init(a_army):
	the_army=a_army
	
	var lbls_box=HBoxContainer.new()
	
	name_lbl=Label.new()
	name_lbl.text=the_army.name
	
	nation_lbl=Label.new()
	nation_lbl.text=the_army.nation
	
	size_lbl=Label.new()
	size_lbl.text=str(the_army.size)
	
	quality_lbl=Label.new()
	quality_lbl.text=str(the_army.quality)
	
	stance_lbl=Label.new()
	stance_lbl.text=the_army.get_stance_as_str()
	
	lbls_box.add_child(nation_lbl)
	lbls_box.add_child(name_lbl)
	lbls_box.add_child(size_lbl)
	lbls_box.add_child(quality_lbl)
	lbls_box.add_child(stance_lbl)
	
	actions_box = HBoxContainer.new()
	var btn_group = ButtonGroup.new()
	
	var aggressive_btn = StanceButton.new(Constants.Stance.AGGRESSIVE,btn_group,Vector2(30,30),"res://images/sword.jpg")
	var defensive_btn = StanceButton.new(Constants.Stance.DEFENSIVE,btn_group,Vector2(30,30),"res://images/shield.jpg")
	var pacify_btn = StanceButton.new(Constants.Stance.PACIFY,btn_group,Vector2(30,30),"res://images/fist-down.jpg")
	var raiding_btn = StanceButton.new(Constants.Stance.RAIDING,btn_group,Vector2(30,30),"res://images/fire.jpg")
	var guerilla_btn = StanceButton.new(Constants.Stance.GUERILLA,btn_group,Vector2(30,30),"res://images/mask.jpg")
	var move_btn = StanceButton.new(Constants.Stance.MOVING,btn_group,Vector2(30,30),"res://images/move.jpg")
	
	aggressive_btn.pressed.connect(func():set_army_stance(the_army,aggressive_btn.stance,stance_lbl))
	defensive_btn.pressed.connect(func():set_army_stance(the_army,defensive_btn.stance,stance_lbl))
	pacify_btn.pressed.connect(func():set_army_stance(the_army,pacify_btn.stance,stance_lbl))
	raiding_btn.pressed.connect(func():set_army_stance(the_army,raiding_btn.stance,stance_lbl))
	guerilla_btn.pressed.connect(func():set_army_stance(the_army,guerilla_btn.stance,stance_lbl))
	move_btn.pressed.connect(func():set_army_stance(the_army,move_btn.stance,stance_lbl))
	
	
	actions_box.add_child(aggressive_btn)
	actions_box.add_child(defensive_btn)	
	actions_box.add_child(pacify_btn)
	actions_box.add_child(raiding_btn)
	actions_box.add_child(guerilla_btn)
	actions_box.add_child(move_btn)
	
	
	add_child(lbls_box)
	add_child(actions_box)

func _ready():
	for child in actions_box.get_children():
		if child.stance==the_army.stance:
			#This doesn't work for some reason...
			child.button_pressed=true
			#child.emit_signal("pressed")
			child.grab_focus()
