extends Node


# TODO:
# For now, Ill just keep a list of the scripts I want to call. 
# Later I can dynamically find them.
var all_testers : Array[TestRunner] = [
	preload("res://test/TestMilitaryCalculator.gd").new()
]

func run_all_tests():
	for tester in all_testers:
		tester.test_all()
		print("\n")
	print("DONE")

func _pressed():
	run_all_tests()
