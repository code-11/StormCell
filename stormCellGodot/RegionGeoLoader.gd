extends Node2D

var SCALE=1
var LONGEST_EXTENT=null
var SMALLEST_EXTENT=null
var ARMY_SPACING=null

var adjacency: Dictionary = {}
var _adjacency_helper = preload("res://RegionAdjacency.gd").new()
var _graph_search = preload("res://GraphSearch.gd").new()

var REGION_LIST_PATH="res://data/region_list.txt"
var REGION_TERRAIN_PATH="res://data/region_terrain.json"
var TERRAIN_DATA_PATH="res://data/terrain_data.json"

func get_the_map():
	return get_parent()

func get_clicked_region(clicked_point):
	for region in get_children():
		for poly in get_polys(region):
			if Geometry2D.is_point_in_polygon(clicked_point,poly.polygon):
				return region
	return null

func point_in_bbox(point: Vector2, bb) -> bool:
	var maxx=bb[0]
	var maxy=bb[1]
	var minx=bb[2]
	var miny=bb[3]
	return minx <= point.x <= maxx and miny <= point.y <= maxy

func long_extent(region):
	var bb=get_region_bb(region)
	var maxx=bb[0]
	var maxy=bb[1]
	var minx=bb[2]
	var miny=bb[3]
	var xdif=maxx-minx
	var ydif=maxy-miny
	if xdif > ydif:
		return xdif
	else:
		return ydif

func get_region_bb(region):
	var maxx=null
	var maxy=null
	var minx=null
	var miny=null
	for poly in get_polys(region):
		for vec in poly.polygon:
			var x=vec[0]
			var y=vec[1]
			if maxx == null or maxx<x:
				maxx=x
			if maxy == null or maxy<y:
				maxy=y
			if minx == null or minx>x:
				minx=x
			if miny == null or miny>y:
				miny=y
	return [maxx,maxy,minx,miny]
	
func get_bb_center(bb):
	var maxx=bb[0]
	var maxy=bb[1]
	var minx=bb[2]
	var miny=bb[3]
	return [(maxx+minx)/2,(maxy+miny)/2]	
	
func get_polys(region):
	var to_return=[]
	for child in region.get_children():
		if child.is_in_group("Polys"):
			to_return.append(child)
	return to_return
	
func get_borders(region):
	var to_return=[]
	for child in region.get_children():
		if child.is_in_group("Borders"):
			to_return.append(child)
	return to_return

func get_armies_and_their_regions()-> MultiMap:
	var to_return=MultiMap.new()
	for region in get_children():
		for child in region.get_children():
			if child.is_in_group(SCConstants.ARMY_GROUP):
				to_return.add(region,child)
	return to_return

func get_armies(region):
	var to_return=[]
	for child in region.get_children():
		if child.is_in_group(SCConstants.ARMY_GROUP):
			to_return.append(child)
	return to_return

func array_to_packed_vec2(array):
	var to_return=PackedVector2Array()
	for el in array:
		to_return.append(Vector2(el[0]/SCALE,el[1]/SCALE))
	return to_return

#func create_region_geometry(polygon_list):
	#var the_poly=Polygon2D.new()
	#for polygon in polygon_list:
		#the_poly.polygons=array_to_packed_vec2(polygon)
	#return the_poly

func create_region_geometry(region_id, polygon_list):
	#var region_geometry=Node2D.new()
	#region_geometry.name=region_id
	#region_geometry.set_script(load("res://region_data.gd"))
	var region_geometry = Region.new()
	region_geometry.name = region_id
	
	var i=0
	for polygon in polygon_list:
		var single_poly=Polygon2D.new()
		var poly_points=array_to_packed_vec2(polygon)
		single_poly.add_to_group("Polys")
		single_poly.polygon=poly_points
		single_poly.name="poly-%s" % i
		region_geometry.add_child(single_poly)
		
		var border = Line2D.new()
		border.add_to_group("Borders")
		border.points=poly_points
		border.width=2
		border.default_color=Color.html(get_the_map().DEFAULT_BORDER_COLOR)
		border.name="border-%s" % i
		region_geometry.add_child(border)
		i+=1
	return region_geometry
	
func read_regions():
	var region_list_file = FileAccess.open(REGION_LIST_PATH, FileAccess.READ)
	var data = JSON.parse_string(region_list_file.get_as_text())
	var regions=Array()
	for region_id in data:
		var region_geometry=create_region_geometry(region_id, data[region_id])
		regions.append(region_geometry)
	return regions
	
	
func read_terrain_data():
	var terrain_data_file = FileAccess.open(TERRAIN_DATA_PATH, FileAccess.READ)
	var terrain_data = JSON.parse_string(terrain_data_file.get_as_text())
	return terrain_data	
	
func read_regional_terrain():
	var region_terrain_file = FileAccess.open(REGION_TERRAIN_PATH, FileAccess.READ)
	var region_terrain_data = JSON.parse_string(region_terrain_file.get_as_text())
	return region_terrain_data

func create_regions(regions_to_nations_dict):
	var regions=read_regions()
	var regional_terrain_data=read_regional_terrain()
	var terrain_data=read_terrain_data()
	print("Num Regions: %s" % regions.size())
	var greatest_extent=0
	var smallest_extent=INF
	for region in regions:
		var terrain_type_for_region=regional_terrain_data[region.name]
		region.terrain = Terrain.from_json_dict(terrain_type_for_region,terrain_data[terrain_type_for_region])
		region.nation = regions_to_nations_dict.get(region.name,null)
		var long_ext=long_extent(region)
		if greatest_extent < long_ext:
			greatest_extent = long_ext
		if smallest_extent > long_ext:
			smallest_extent = long_ext
		add_child(region)
	LONGEST_EXTENT=greatest_extent
	SMALLEST_EXTENT=smallest_extent
	ARMY_SPACING=max(SMALLEST_EXTENT/4.0, 15.0)
	print(LONGEST_EXTENT)
	adjacency = _adjacency_helper.build_adjacency_graph(get_children())
	print("Adjacency graph built: %s regions" % adjacency.size())

func color_region(region,color_hex):
	var polys=region.get_children()
	for poly in polys:
		if poly is Polygon2D:
			poly.color=Color.html(color_hex)

func color_regions(region_color_dict):
	for region in get_children():
		var region_color_hex=region_color_dict.get(region.name,get_the_map().UNOCCUPIED_REGION_COLOR)
		color_region(region,region_color_hex)

func color_border(region,color_hex):
	var borders=get_borders(region)
	for border in borders:
		border.default_color=Color.html(color_hex)

func find_army_region(army_node):
	#TODO HMMMM
	return army_node.get_parent()

func move_army(army,destination_region, cur_day):
	var army_cur_region = find_army_region(army)
	army_cur_region.remove_child(army)

	var move_duration=army_movement_day_cost(destination_region)
	army.stance_lock=cur_day + move_duration

	var bb_center=get_bb_center(get_region_bb(destination_region))
	army.position=Vector2(bb_center[0],bb_center[1])
	destination_region.add_child(army)

	update_army_positions(army_cur_region)
	update_army_positions(destination_region)
	

func army_movement_day_cost(region):
	var mobility_mult=(1-region.terrain.mobility)*10+1
	var days = mobility_mult * SCConstants.BASE_MOVE_MULT
	return days
 
func attach_army(army_node,region):
	for child_region in get_children():
		if child_region.name == region:
			var bb_center=get_bb_center(get_region_bb(child_region))
			army_node.position=Vector2(bb_center[0],bb_center[1])
			child_region.add_child(army_node)
			update_army_positions(child_region)
			return
	push_error("Could not find region for "+army_node.name+" "+region)

func _position_stack(armies, base_pos):
	var total_height=(armies.size()-1)*ARMY_SPACING
	var start_y=base_pos.y-total_height/2.0
	for i in range(armies.size()):
		armies[i].position=Vector2(base_pos.x, start_y+i*ARMY_SPACING)

func update_army_positions(region):
	if ARMY_SPACING==null:
		return
	var armies=get_armies(region)
	if armies.is_empty():
		return

	var bb_center=get_bb_center(get_region_bb(region))
	var center=Vector2(bb_center[0],bb_center[1])

	for army in armies:
		army.set_in_battle(false)

	var by_nation={}
	for army in armies:
		if not by_nation.has(army.nation):
			by_nation[army.nation]=[]
		by_nation[army.nation].append(army)

	var nations=by_nation.keys()

	if nations.size()==1:
		_position_stack(by_nation[nations[0]], center)
	else:
		# First army of each of the two opposing nations fights in the center
		var nation_a=nations[0]
		var nation_b=nations[1]
		var fighter_a=by_nation[nation_a][0]
		var fighter_b=by_nation[nation_b][0]
		fighter_a.set_in_battle(true)
		fighter_b.set_in_battle(true)
		fighter_a.position=center+Vector2(-ARMY_SPACING/2.0, 0)
		fighter_b.position=center+Vector2(ARMY_SPACING/2.0, 0)

		# Remaining armies (extras from any nation) circle around center
		var remaining_by_nation={}
		for nation in nations:
			var start_idx=1 if (nation==nation_a or nation==nation_b) else 0
			var remaining=by_nation[nation].slice(start_idx)
			if remaining.size()>0:
				remaining_by_nation[nation]=remaining

		if not remaining_by_nation.is_empty():
			var num_groups=remaining_by_nation.size()
			var circle_radius=ARMY_SPACING*2.0
			var angle_step=TAU/num_groups
			var g_idx=0
			for nation in remaining_by_nation:
				var angle=angle_step*g_idx-PI/2.0
				var group_center=center+Vector2(
					circle_radius*cos(angle),
					circle_radius*sin(angle)
				)
				_position_stack(remaining_by_nation[nation], group_center)
				g_idx+=1

#TODO: this doens't belong here!
func battle_init(region, armies):
	# armies must be co-located
	var army1=armies[0]
	var army2=armies[1]
	
	var attacker_and_defender =MilitaryCalculator.determine_attacker(army1, army2, region)
	var attacker=attacker_and_defender[0]
	var defender=attacker_and_defender[1]
	print(attacker_and_defender)
	var dmgs=MilitaryCalculator.calculate_one_day_battle(attacker,defender, region)
	var dead_armies=[]
	# Assign Damage
	if attacker.size-dmgs[0]<=1:
		dead_armies.append(attacker)
	else:
		attacker.size-=dmgs[0]
		
	if defender.size-dmgs[1]<=1:
		# You can have a simultaneous kill I think.
		dead_armies.append(defender)
	else:
		defender.size-=dmgs[1]	
	return dead_armies
	
	
func possible_battle_init(region, armies):
	# Returns a list of armies that have been destroyed
	if len(armies)<2:
		return []
	# armies must be co-located
	if len(armies)==2:
		#TODO: check if they're actually hostile!
		return battle_init(region, armies)
	else:
		print("Multi battle not implemented!")		

func _get_cur_day():
	return get_node("/root/Node2D/TheGame").get_cur_day()

func initiate_army_move(army, destination_region) -> void:
	var current_region = find_army_region(army)
	if current_region == destination_region:
		return
	var cost_fn = Callable(self, "army_movement_day_cost")
	var path = _graph_search.dijkstra(current_region, destination_region, adjacency, cost_fn)
	if path.is_empty():
		print("No path found to destination")
		return
	army.move_queue = path
	army.stance = SCConstants.Stance.MOVING
	_advance_army_one_step(army, _get_cur_day())

func _advance_army_one_step(army, cur_day) -> void:
	if army.move_queue.is_empty():
		return
	var next_region = army.move_queue.pop_front()
	move_army(army, next_region, cur_day)
	if army.in_battle:
		army.move_queue.clear()
		return
	if army.move_queue.is_empty():
		army.stance = SCConstants.Stance.AGGRESSIVE

func advance_all_moving_armies(cur_day) -> void:
	for region in get_children():
		for army in get_armies(region):
			if army.stance == SCConstants.Stance.MOVING \
			   and army.move_queue.size() > 0 \
			   and army.can_change_stance():
				_advance_army_one_step(army, cur_day)

func _ready():
	pass
func _process(delta):
	pass
