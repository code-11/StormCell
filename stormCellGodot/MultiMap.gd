class_name MultiMap

var _data={}
	
	
func keys():
	return self._data.keys()	
	
func add(new_key, new_value):
	var inner_list=self._data.get(new_key,[])
	inner_list.append(new_value)
	self._data[new_key]=inner_list
	
func extend(the_key,the_list):
	var inner_list=self._data.get(the_key,[])
	inner_list.append_array(the_list)
	self._data[the_key]=inner_list
	
#Apply a funciton to whole list for a key, returning a new, possibly smaller list for the key
#func_ref takes (key,value) where value is a list
func map(func_ref):
	var to_return= MultiMap.new()
	for key in self._data:
		var value=self._data[key]
		to_return.extend(key,func_ref.call(key, value))
	return to_return
	
func get_size():
	var cumulative_size=0
	for key in self._data:
		var value=self._data[key]
		cumulative_size+=value.size()
	return cumulative_size
	
#func_ref takes (key, value)
func apply(func_ref):
	for key in self._data:
		var inner_list=self._data[key]
		for value in inner_list:
			func_ref.call(key, value)
	
func _to_string():
	var to_return="{\n"
	for key in self._data:
		var value=self._data[key]
		to_return+= " "+str(key) +" : " + str(value) + "\n"
	to_return += "}" 
	return to_return
	
func get_keyset():
	return self._data.keys
