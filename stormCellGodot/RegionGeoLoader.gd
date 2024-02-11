extends Node2D

var SCALE=1
var LONGEST_EXTENT=null

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
		if child is Polygon2D:
			to_return.append(child)
	return to_return
	
func get_borders(region):
	var to_return=[]
	for child in region.get_children():
		if child is Line2D:
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
	var region_geometry=Node2D.new()
	region_geometry.name=region_id
	region_geometry.set_script(load("res://region_data.gd"));
	
	var i=0
	for polygon in polygon_list:
		var single_poly=Polygon2D.new()
		var poly_points=array_to_packed_vec2(polygon)
		single_poly.polygon=poly_points
		single_poly.name="poly-%s" % i
		region_geometry.add_child(single_poly)
		
		var border = Line2D.new()
		border.points=poly_points
		border.width=2
		border.default_color=Color.html(get_the_map().DEFAULT_BORDER_COLOR)
		border.name="border-%s" % i
		region_geometry.add_child(border)
		i+=1
	return region_geometry
	
func read_regions():
	var region_list_file = FileAccess.open("res://region_list.txt", FileAccess.READ)
	var data = JSON.parse_string(region_list_file.get_as_text())
	var regions=Array()
	for region_id in data:
		var region_geometry=create_region_geometry(region_id, data[region_id])
		regions.append(region_geometry)
	return regions
	
func read_regional_terrain():
	var region_terrain_file = FileAccess.open("res://region_terrain.json", FileAccess.READ)
	var region_terrain_data = JSON.parse_string(region_terrain_file.get_as_text())
	return region_terrain_data

func create_regions():
	var regions=read_regions()
	var terrain_data=read_regional_terrain()
	print("Num Regions: %s" % regions.size())
	var greatest_extent=0
	for region in regions:
		region.terrain = terrain_data[region.name]
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

func _ready():
	pass
func _process(delta):
	pass
