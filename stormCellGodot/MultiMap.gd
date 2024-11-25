class_name MultiMap

var _data={}
	
func add(new_key, new_value):
	var inner_list=self._data.get(new_key,[])
	inner_list.append(new_key)
	self._data[new_key]=inner_list
	
func map(func_ref):
	for key in self._data:
		var value=self._data[key]
		func_ref.call(value)
	
func _to_string():
	var to_return="{\n"
	for key in self._data:
		var value=self._data[key]
		to_return+= " "+str(key) +" : " + str(value) + "\n"
	to_return += "}" 
	return to_return
	
func get_keyset():
	return self._data.keys
