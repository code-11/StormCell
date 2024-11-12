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

func test_full_mult_1():
	print("	Testing test_full_mult_1")
	var attacker = Army.new("attacker",null,"black",1)
	attacker.stance = SCConstants.Stance.RAIDING
	var defender = Army.new("defender",null,"black",1)
	defender.stance = SCConstants.Stance.GUERILLA
	var region=Region.new();
	region.terrain=Terrain.new("Mountains", "#362910", 2, .1, 1.3)
	var mult=mil_calc.calculate_full_multiplier(attacker,defender,region)
	var expected_mult=mil_calc.DEF * .5 #.165
	assert(mult==expected_mult)
	
func test_full_mult_2():
	print("	Testing test_full_mult_2")
	var attacker = Army.new("attacker",null,"black",1)
	attacker.stance = SCConstants.Stance.PACIFY
	var defender = Army.new("defender",null,"black",1)
	defender.stance = SCConstants.Stance.AGGRESSIVE
	var region=Region.new();
	region.terrain= Terrain.new("Forest", "#14430c", 1.7, .3, 1.1) 
	var mult=mil_calc.calculate_full_multiplier(attacker,defender,region)
	var expected_mult=mil_calc.DEF_II * (1/1.7) #~.118
	assert(mult==expected_mult)
	
func test_full_mult_3():
	print("	Testing test_full_mult_2")
	var attacker = Army.new("attacker",null,"black",1)
	attacker.stance = SCConstants.Stance.AGGRESSIVE
	var defender = Army.new("defender",null,"black",1)
	defender.stance = SCConstants.Stance.PACIFY
	var region=Region.new();
	region.terrain= Terrain.new("Desert", "#d08f55", .5, 1.6, 5)
	var mult=mil_calc.calculate_full_multiplier(attacker,defender,region)
	var expected_mult=mil_calc.ATK_II * 2 #10
	assert(mult==expected_mult)

func test_all():
	print("Testing Military Calculator")
	test_stance_mult_1()
	test_stance_mult_2()
	test_stance_mult_3()
	test_full_mult_1()
	test_full_mult_2()
	test_full_mult_3()
