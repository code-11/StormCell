from scenarios.scenario_gen_scripts.test_scenario import TestScenario as TheScenario
# from scenarios.x_marks_the_spot_4 import XMarksTheSpot4 as TheScenario


# from scenarios.whirlpool_3 import Whirlpool3 as TheScenario


def export_scenario(scenario):
    name_to_use = scenario.name.replace(' ', '_').lower()
    with open(f"./maps/{name_to_use}.sc_map", 'w', encoding='utf-8') as f:
        f.write(scenario.sc_json_save())


if __name__ == '__main__':
    scenario = TheScenario()
    export_scenario(scenario)
