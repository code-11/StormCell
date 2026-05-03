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

func test_discover_mult_1():
	print("	Testing test_discover_mult_1")
	var attacker = Army.new("attacker",null,"black",1)
	var defender = Army.new("defender",null,"black",1)
	var region=Region.new();
	region.terrain= Terrain.new("Desert", "#d08f55", .5, 1.6, 5)
	var mult=mil_calc.calculate_discover_multiplier(attacker,defender,region)
	var expected_mult=mil_calc.BASE_DISCOVER_CHANCE * 2
	assert(mult==expected_mult) #.1, discovering on a desert is fast, expected in 10 turns

func test_discover_mult_2():
	print("	Testing test_discover_mult_2")
	var attacker = Army.new("attacker",null,"black",1)
	var defender = Army.new("defender",null,"black",1)
	var region=Region.new();
	region.terrain= Terrain.new("Mountains", "#362910", 2, .1, 1.3)
	var mult=mil_calc.calculate_discover_multiplier(attacker,defender,region)
	var expected_mult=mil_calc.BASE_DISCOVER_CHANCE * .5
	assert(mult==expected_mult) #.025, discovering on mountains is slow, expected in 40 turns


func test_determine_attacker():
	print("	Testing test_determine_attacker")
	const nation1="nation1"
	const nation2="nation2"
	var army1 = Army.new("army1",nation1,"black",1)
	var army2 = Army.new("army2",nation2,"black",1)
	var region=Region.new();
	region.nation=nation2
	
	army1.stance=SCConstants.Stance.AGGRESSIVE
	army2.stance=SCConstants.Stance.DEFENSIVE
	var result1=mil_calc.determine_attacker(army2,army1,region)
	#Aggressive is more attacky than defensive, so it should be attacker
	assert(result1==[army1,army2])
	
	army1.stance=SCConstants.Stance.PACIFY
	army2.stance=SCConstants.Stance.RAIDING
	var result2=mil_calc.determine_attacker(army2,army1,region)
	#RAIDING is more attacky than PACIFY, so it should be attacker
	assert(result2==[army2,army1])
	
	army1.stance=SCConstants.Stance.MOVING
	army2.stance=SCConstants.Stance.GUERILLA
	var result3=mil_calc.determine_attacker(army2,army1,region)
	#MOVING is more attacky than GUERILLA, so it should be attacker
	assert(result3==[army1,army2])
	
	army1.stance=SCConstants.Stance.MOVING
	army2.stance=SCConstants.Stance.MOVING
	var result4=mil_calc.determine_attacker(army2,army1,region)
	#Region owned by nation2 so army1 is attacker
	assert(result4==[army1,army2])
	
	#Throw in a ordering test here. Order should not matter
	var result5=mil_calc.determine_attacker(army1,army2,region)
	assert(result5==[army1,army2])
	
	region.nation=nation1
	var result6=mil_calc.determine_attacker(army2,army1,region)
	#Region owned by nation1 now so army2 is attacker
	assert(result6==[army2,army1])
	
	region.nation="neither"
	var result7=mil_calc.determine_attacker(army2,army1,region)
	#Tie breaker makes nation2 the attacker since its string is greater
	assert(result7==[army2,army1])
	
	#Another ordering test
	var result8=mil_calc.determine_attacker(army1,army2,region)
	assert(result8==[army2,army1])
	
	
	

func test_stance_battle_matrix():
	print("	Testing test_stance_battle_matrix")
	print("	Two size-50 armies, neutral plains (defensiveness=1), all 36 stance combos")
	var stances = [
		SCConstants.Stance.AGGRESSIVE,
		SCConstants.Stance.DEFENSIVE,
		SCConstants.Stance.PACIFY,
		SCConstants.Stance.RAIDING,
		SCConstants.Stance.GUERILLA,
		SCConstants.Stance.MOVING
	]
	var stance_names = {
		SCConstants.Stance.AGGRESSIVE: "Aggressive",
		SCConstants.Stance.DEFENSIVE: "Defensive",
		SCConstants.Stance.PACIFY:     "Pacify",
		SCConstants.Stance.RAIDING:    "Raiding",
		SCConstants.Stance.GUERILLA:   "Guerilla",
		SCConstants.Stance.MOVING:     "Moving"
	}
	var region = Region.new()
	region.terrain = Terrain.new("Plains", "#7ec850", 1.0, 1.0, 1.0)
	region.nation = "neutral"

	print("	%-12s vs %-12s | Turns | Died" % ["Army A", "Army B"])
	for stance_a in stances:
		for stance_b in stances:
			var army_a = Army.new("army_a", "nation_a", "#aa0000", 15)
			army_a.stance = stance_a
			army_a.size = 50.0
			var army_b = Army.new("army_b", "nation_b", "#0000aa", 15)
			army_b.stance = stance_b
			army_b.size = 50.0

			var ordered = mil_calc.determine_attacker(army_a, army_b, region)
			var attacker = ordered[0]
			var defender = ordered[1]

			var turns = 0
			while army_a.size >= 1.0 and army_b.size >= 1.0 and turns < 1000:
				var dmg = mil_calc.calculate_one_day_battle(attacker, defender, region)
				attacker.size -= dmg[0]
				defender.size -= dmg[1]
				turns += 1

			var died: String
			var survivor_hp: String
			if army_a.size < 1.0 and army_b.size < 1.0:
				died = "both"
				survivor_hp = "none"
			elif army_a.size < 1.0:
				died = "army_a (%s)" % stance_names[stance_a]
				survivor_hp = "%.1f" % army_b.size
			elif army_b.size < 1.0:
				died = "army_b (%s)" % stance_names[stance_b]
				survivor_hp = "%.1f" % army_a.size
			else:
				died = "timeout"
				survivor_hp = "n/a"

			print("	%-12s vs %-12s |  %3d  | %-28s | survivor hp: %s" % [
				stance_names[stance_a], stance_names[stance_b], turns, died, survivor_hp
			])

func test_all():
	print("Testing Military Calculator")
	test_stance_mult_1()
	test_stance_mult_2()
	test_stance_mult_3()
	test_full_mult_1()
	test_full_mult_2()
	test_full_mult_3()
	test_discover_mult_1()
	test_discover_mult_2()
	test_determine_attacker()
	test_stance_battle_matrix()
