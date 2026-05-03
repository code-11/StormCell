extends TestRunner

var graph_search = preload("res://GraphSearch.gd").new()
var geo_loader = preload("res://RegionGeoLoader.gd").new()

# Terrain helpers — mobility drives army_movement_day_cost:
#   cost = ((1 - mobility) * 10 + 1) * BASE_MOVE_MULT(3)
# Plains  mobility=1.0 -> cost = 3
# Hills   mobility=0.7 -> cost = 12
# Forest  mobility=0.3 -> cost = 24
# Mountains mobility=0.1 -> cost = 30

func _plains_region():
	var r = Region.new()
	r.terrain = Terrain.new("Plains", "#7ec850", 1.0, 1.0, 1.0)
	return r

func _hills_region():
	var r = Region.new()
	r.terrain = Terrain.new("Hills", "#8ab34e", 1.5, 0.7, 1.0)
	return r

func _forest_region():
	var r = Region.new()
	r.terrain = Terrain.new("Forest", "#14430c", 1.7, 0.3, 1.1)
	return r

func _mountain_region():
	var r = Region.new()
	r.terrain = Terrain.new("Mountains", "#362910", 2.0, 0.1, 1.3)
	return r

# --- movement cost per region ---

func test_movement_cost_plains():
	print("	Testing test_movement_cost_plains")
	var region = _plains_region()
	assert(geo_loader.army_movement_day_cost(region) == 3)

func test_movement_cost_hills():
	print("	Testing test_movement_cost_hills")
	var region = _hills_region()
	assert(geo_loader.army_movement_day_cost(region) == 12)

func test_movement_cost_forest():
	print("	Testing test_movement_cost_forest")
	var region = _forest_region()
	assert(geo_loader.army_movement_day_cost(region) == 24)

func test_movement_cost_mountains():
	print("	Testing test_movement_cost_mountains")
	var region = _mountain_region()
	assert(geo_loader.army_movement_day_cost(region) == 30)

# --- total days for a multi-hop path ---

func _path_total_days(path: Array) -> int:
	var total = 0
	for region in path:
		total += geo_loader.army_movement_day_cost(region)
	return total

func test_three_plains_hops():
	print("	Testing test_three_plains_hops")
	# 3 plains steps: 3+3+3 = 9 days
	var path = [_plains_region(), _plains_region(), _plains_region()]
	assert(_path_total_days(path) == 9)

func test_plains_then_mountain():
	print("	Testing test_plains_then_mountain")
	# 2 plains then 1 mountain: 3+3+30 = 36 days
	var path = [_plains_region(), _plains_region(), _mountain_region()]
	assert(_path_total_days(path) == 36)

func test_mixed_terrain_path():
	print("	Testing test_mixed_terrain_path")
	# plains(3) + hills(12) + forest(24) + mountains(30) = 69 days
	var path = [_plains_region(), _hills_region(), _forest_region(), _mountain_region()]
	assert(_path_total_days(path) == 69)

# --- dijkstra path selection ---

func test_dijkstra_returns_empty_for_same_node():
	print("	Testing test_dijkstra_returns_empty_for_same_node")
	var a = "a"
	var path = graph_search.dijkstra(a, a, {a: []}, func(_r): return 1.0)
	assert(path == [])

func test_dijkstra_returns_empty_when_unreachable():
	print("	Testing test_dijkstra_returns_empty_when_unreachable")
	var a = "a"
	var b = "b"
	var path = graph_search.dijkstra(a, b, {a: [], b: []}, func(_r): return 1.0)
	assert(path == [])

func test_dijkstra_single_hop():
	print("	Testing test_dijkstra_single_hop")
	var a = "a"
	var b = "b"
	var adjacency = {a: [b], b: [a]}
	var path = graph_search.dijkstra(a, b, adjacency, func(_r): return 3.0)
	assert(path == [b])

func test_dijkstra_simple_chain():
	print("	Testing test_dijkstra_simple_chain")
	# A - B - C (linear, equal cost): path should be [B, C]
	var a = "a"; var b = "b"; var c = "c"
	var adjacency = {a: [b], b: [a, c], c: [b]}
	var path = graph_search.dijkstra(a, c, adjacency, func(_r): return 3.0)
	assert(path == [b, c])

func test_dijkstra_prefers_cheaper_terrain():
	print("	Testing test_dijkstra_prefers_cheaper_terrain")
	# A connects to: B (mountain shortcut, 30 days) and D (plains detour start, 3 days)
	# B -> C (3 days). D -> C (3 days).
	# Direct:  A->B->C = 30+3 = 33 days
	# Detour:  A->D->C = 3+3  =  6 days  <-- dijkstra should pick this
	var a = "a"; var b = "b"; var c = "c"; var d = "d"
	var adjacency = {a: [b, d], b: [a, c], c: [b, d], d: [a, c]}
	var costs = {a: 0.0, b: 30.0, c: 3.0, d: 3.0}
	var path = graph_search.dijkstra(a, c, adjacency, func(r): return costs[r])
	assert(path == [d, c])

func test_dijkstra_avoids_mountain_bottleneck():
	print("	Testing test_dijkstra_avoids_mountain_bottleneck")
	# A connects to B and C. B->D(plains). C->D(plains) but C is a mountain.
	# A->B->D = 3+3 = 6 days
	# A->C->D = 30+3 = 33 days
	# Dijkstra should pick A->B->D
	var a = "a"; var b = "b"; var c = "c"; var d = "d"
	var adjacency = {a: [b, c], b: [a, d], c: [a, d], d: [b, c]}
	var costs = {a: 0.0, b: 3.0, c: 30.0, d: 3.0}
	var path = graph_search.dijkstra(a, d, adjacency, func(r): return costs[r])
	assert(path == [b, d])

func test_all():
	print("Testing Movement")
	test_movement_cost_plains()
	test_movement_cost_hills()
	test_movement_cost_forest()
	test_movement_cost_mountains()
	test_three_plains_hops()
	test_plains_then_mountain()
	test_mixed_terrain_path()
	test_dijkstra_returns_empty_for_same_node()
	test_dijkstra_returns_empty_when_unreachable()
	test_dijkstra_single_hop()
	test_dijkstra_simple_chain()
	test_dijkstra_prefers_cheaper_terrain()
	test_dijkstra_avoids_mountain_bottleneck()
