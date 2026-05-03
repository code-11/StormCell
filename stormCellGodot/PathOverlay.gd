extends Node2D

func _draw():
	var geo = get_parent()
	var gui = get_node_or_null("/root/Node2D/TheGame/GuiCtrl")
	if gui == null or gui.selected_region == null:
		return
	var selected = gui.selected_region
	for army in geo.get_armies(selected):
		if army.move_queue.is_empty():
			continue
		var cur = geo.get_bb_center(geo.get_region_bb(selected))
		var prev = Vector2(cur[0], cur[1])
		for region in army.move_queue:
			var next_c = geo.get_bb_center(geo.get_region_bb(region))
			var next = Vector2(next_c[0], next_c[1])
			draw_dashed_line(prev, next, Color.BLACK, 2.0, 8.0)
			prev = next

func _process(_delta):
	queue_redraw()
