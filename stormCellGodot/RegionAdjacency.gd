extends RefCounted

class_name RegionAdjacency

func build_adjacency_graph(regions_array: Array) -> Dictionary:
	var adjacency := {}
	for region in regions_array:
		adjacency[region] = []
	for i in range(regions_array.size()):
		for j in range(i + 1, regions_array.size()):
			if _regions_are_adjacent(regions_array[i], regions_array[j]):
				adjacency[regions_array[i]].append(regions_array[j])
				adjacency[regions_array[j]].append(regions_array[i])
	return adjacency

func _regions_are_adjacent(region_a, region_b) -> bool:
	for poly_a in _get_polys(region_a):
		for expanded in Geometry2D.offset_polygon(poly_a.polygon, 2.0):
			for poly_b in _get_polys(region_b):
				if Geometry2D.intersect_polygons(expanded, poly_b.polygon).size() > 0:
					return true
	return false

func _get_polys(region) -> Array:
	var result := []
	for child in region.get_children():
		if child.is_in_group("Polys") and child is Polygon2D:
			result.append(child)
	return result
