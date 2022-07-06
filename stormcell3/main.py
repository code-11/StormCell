import pygame, sys
from pygame.locals import *
from scbutton import SCButton
# from Scenarios.test_scenario import TestScenario as TheScenario
# from Scenarios.x_marks_the_spot_4 import XMarksTheSpot4 as TheScenario
from Scenarios.whirlpool_3 import Whirlpool3 as TheScenario
from gui_utils import auto_text

LEFT_BTN = 1
MIDDLE_BTN = 2
RIGHT_BTN = 3


def draw_outliner(window, scenario, font, selected_node, text_save_map):
    pygame.draw.line(window, 'white', (800, 0), (800, 600))

    turn_text = scenario.get_cur_turn_text()
    auto_text("turn-counter", window, text_save_map, font, turn_text, (820, 10))

    y_pos = 40
    for nation in scenario.nations:
        text_id = f"{nation.name}-gold"
        defeated_string = '(Dead)' if scenario.defeated[nation.name] else ''
        auto_text(text_id, window, text_save_map, font, f"{defeated_string} {nation.name} gold: {nation.gold}",
                  (870, y_pos))
        y_pos += 17

    btn1 = SCButton('buy-city', Rect(820, 120, 150, 60), font, 'Make City: \n Cost 10G, +4G/Turn')
    btn1.on_click = lambda: scenario.possibly_build_at_node(selected_node, "C")

    btn2 = SCButton('buy-manu', Rect(820, 220, 150, 60), font, 'Make Manufactory: \n Cost 10G, \n +1Army/-4G/Turn ')
    btn2.on_click = lambda: scenario.possibly_build_at_node(selected_node, "M")

    btn3 = SCButton('buy-fort', Rect(820, 320, 150, 60), font, 'Make Fort: \n Cost 10G, x1.5 Def')
    btn3.on_click = lambda: scenario.possibly_build_at_node(selected_node, "F")

    btn4 = SCButton('destroy', Rect(820, 420, 150, 40), font, 'Raze own building')
    btn4.on_click = lambda: scenario.possibly_destroy_build_at_node(selected_node)

    btn5 = SCButton('next-turn', Rect(800, 540, 200, 60), font, 'Next Turn')
    btn5.on_click = scenario.incr_turn_and_check_for_end

    buttons = [btn1, btn2, btn3, btn4, btn5]

    for btn in buttons:
        btn.draw_button(window, text_save_map)

    return buttons


def exit():
    pygame.quit()
    sys.exit()


def quit():
    pygame.quit()
    sys.exit()


def run():
    pygame.init()
    window = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption('StormCell3')

    scenario = TheScenario()
    scenario.set_all_undefeated()

    # font = pygame.freetype.Font("C:\\Users\\brend\\Documents\\StormCell\\stormCell3\\resources\\fonts\\vecna\\Vecna.otf", 12)
    font = pygame.freetype.SysFont('Verdana', 12)
    selected_node = None
    text_save_map = {}
    end_btn = None

    while True:  # main game loop
        buttons = draw_outliner(window, scenario, font, selected_node, text_save_map)

        if scenario.winning_nation is not None:
            winning_text = f" {scenario.winning_nation.name} has won! \n (Click here to exit) "
            end_btn = SCButton('end-btn', Rect(500, 300, 200, 60), font, winning_text, text_color='black',
                               background_color='white')
            end_btn.on_click = exit
            buttons.clear()
            buttons.append(end_btn)

        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()

            if event.type == MOUSEBUTTONDOWN and event.button == LEFT_BTN:
                for btn in buttons:
                    btn.click_test(mouse)

                new_selected_node = scenario.click_test(mouse)

                if new_selected_node is not None:
                    if selected_node is not None:
                        selected_node.undraw_as_selected(window)
                    selected_node = new_selected_node

            if event.type == MOUSEBUTTONDOWN and event.button == RIGHT_BTN and selected_node is not None:
                destination_node = scenario.click_test(mouse)
                scenario.move_command(selected_node, destination_node)

        # TODO: Because things only happen on clicks, we *could* gate all refresh behind clicking
        for node in scenario.nodes:
            node.draw_connections(window)
        for node in scenario.nodes:
            node.draw_node(window, font)

        if selected_node is not None:
            selected_node.draw_as_selected(window)

        if end_btn is not None:
            end_btn.draw_button(window, text_save_map)

        pygame.display.update()


if __name__ == '__main__':
    run()
