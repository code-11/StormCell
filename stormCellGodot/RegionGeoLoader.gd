extends Node2D

var SCALE=1
var LONGEST_EXTENT=null

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
			if child.is_in_group("Armies"):
				to_return.add(region,child)
	return to_return

func get_armies(region):
	var to_return=[]
	for child in region.get_children():
		if child.is_in_group("Armies"):
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
	#region_geometry.set_script(load("res://region_data.gd"));
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
	for region in regions:
		var terrain_type_for_region=regional_terrain_data[region.name]
		region.terrain = Terrain.from_json_dict(terrain_type_for_region,terrain_data[terrain_type_for_region])
		region.nation = regions_to_nations_dict.get(region.name,null)
		var long_extent=long_extent(region)
		if greatest_extent < long_extent:
			greatest_extent = long_extent
		add_child(region)
	LONGEST_EXTENT=greatest_extent
	print(LONGEST_EXTENT)

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

func move_army(army,destination_region):
	var army_cur_region = find_army_region(army)
	army_cur_region.remove_child(army)
	var bb_center=get_bb_center(get_region_bb(destination_region))
	army.position=Vector2(bb_center[0],bb_center[1])
	destination_region.add_child(army)

func attach_army(army_node,region):
	for child_region in get_children():
		if child_region.name == region:
			var bb_center=get_bb_center(get_region_bb(child_region))
			army_node.position=Vector2(bb_center[0],bb_center[1])
			child_region.add_child(army_node)
			return
	push_error("Could not find region for "+army_node.name+" "+region)

#TODO: this doens't belong here!
func battle_init(region, armies):
	# armies must be co-located
	var army1=armies[0]
	var army2=armies[1]
	var attacker_defender=MilitaryCalculator.determine_attacker(region, army1, army2)
	print("Doing battle!")
	print(armies)
	print(attacker_defender)
	
func possible_battle_init(region, armies):
	if len(armies)<2:
		return
	# armies must be co-located
	if len(armies)==2:
		#TODO: check if they're actually hostile!
		battle_init(region, armies)
	else:
		print("Multi battle not implemented!")		

func _ready():
	pass
func _process(delta):
	pass
