extends TestRunner

var mil_calc = preload("res://MilitaryCalculator.gd").new()


func test_stance_mult_1():
	print("	Testing test_stance_mult1")
	var attacker = Army.new("attacker",null,"black",1)
	attacker.stance = SCConstants.Stance.AGGRESSIVE
	var defender = Army.new("defender",null,"black",1)
	defender.stance = SCConstants.Stance.DEFENSIVE
	var mult=mil_calc.calculate_stance_multiplier(attacker,defender)
	assert(mult==mil_calc.DEF)
	
func test_stance_mult_2():
	print("	Testing test_stance_mult2")
	var attacker = Army.new("attacker",null,"black",1)
	attacker.stance = SCConstants.Stance.AGGRESSIVE
	var defender = Army.new("defender",null,"black",1)
	defender.stance = SCConstants.Stance.GUERILLA
	var mult=mil_calc.calculate_stance_multiplier(attacker,defender)
	assert(mult==mil_calc.DEF_I)
	
func test_stance_mult_3():
	print("	Testing test_stance_mult3")
	var attacker = Army.new("attacker",null,"black",1)
	attacker.stance = SCConstants.Stance.GUERILLA
	var defender = Army.new("defender",null,"black",1)
	defender.stance = SCConstants.Stance.MOVING
	var mult=mil_calc.calculate_stance_multiplier(attacker,defender)
	assert(mult==mil_calc.ATK_II)

func test_all():
	print("Testing Military Calculator")
	test_stance_mult_1()
	test_stance_mult_2()
	test_stance_mult_3()
