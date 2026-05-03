extends RefCounted

class_name GraphSearch

func dijkstra(start, destination, adjacency: Dictionary, cost_fn: Callable) -> Array:
	if start == destination:
		return []
	var dist := { start: 0.0 }
	var parent := {}
	var visited := {}
	var heap := [[0.0, start]]

	while heap.size() > 0:
		heap.sort()
		var entry = heap.pop_front()
		var cost: float = entry[0]
		var current = entry[1]
		if visited.has(current):
			continue
		visited[current] = true
		if current == destination:
			return _reconstruct_path(start, destination, parent)
		for neighbor in adjacency.get(current, []):
			if visited.has(neighbor):
				continue
			var new_cost: float = cost + cost_fn.call(neighbor)
			if not dist.has(neighbor) or new_cost < dist[neighbor]:
				dist[neighbor] = new_cost
				parent[neighbor] = current
				heap.append([new_cost, neighbor])
	return []

func _reconstruct_path(start, destination, parent) -> Array:
	var path := []
	var current = destination
	while current != start:
		path.push_front(current)
		current = parent[current]
	return path
