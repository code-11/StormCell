extends Node2D

var SCALE=1

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
	
	for polygon in polygon_list:
		var single_poly=Polygon2D.new()
		var poly_points=array_to_packed_vec2(polygon)
		single_poly.polygon=poly_points
		region_geometry.add_child(single_poly)
		
		var border = Line2D.new()
		border.points=poly_points
		border.width=3
		border.default_color=Color(0,0,0)
		region_geometry.add_child(border)
	return region_geometry
	
func read_regions():
	var region_list_file = FileAccess.open("res://region_list.txt", FileAccess.READ)
	var data = JSON.parse_string(region_list_file.get_as_text())
	var regions=Array()
	for region_id in data:
		var region_geometry=create_region_geometry(region_id, data[region_id])
		regions.append(region_geometry)
	return regions

func create_regions():
	var regions=read_regions()
	print(regions.size())
	for region in regions:
		add_child(region)

func color_region(region,color_hex):
	var polys=region.get_children()
	for poly in polys:
		if poly is Polygon2D:
			poly.color=Color.html(color_hex)

func color_regions(region_color_dict):
	print(region_color_dict)
	for region in get_children():
		var region_color_hex=region_color_dict.get(region.name,"#D5CEAB")
		color_region(region,region_color_hex)

func _ready():
	pass
func _process(delta):
	pass
