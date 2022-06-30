import pygame, sys
from pygame.locals import *
from scbutton import SCButton
# from Scenarios.test_scenario import TestScenario as TheScenario
from Scenarios.x_marks_the_spot_4 import XMarksTheSpot4 as TheScenario


def draw_outliner(window, scenario, font, selected_node):
    pygame.draw.line(window, 'white', (800, 0), (800, 600))

    btn1 = SCButton(Rect(820, 120, 150, 60), font, 'Make City')
    btn1.on_click = lambda: scenario.possibly_build_at_node(selected_node, "C")

    btn2 = SCButton(Rect(820, 220, 150, 60), font, 'Make Manufactory')
    btn2.on_click = lambda: scenario.possibly_build_at_node(selected_node, "M")

    btn3 = SCButton(Rect(820, 320, 150, 60), font, 'Make Fort')
    btn3.on_click = lambda: scenario.possibly_build_at_node(selected_node, "F")

    btn4 = SCButton(Rect(800, 540, 200, 60), font, 'Next Turn')
    btn4.on_click = scenario.incr_turn

    buttons = [btn1, btn2, btn3, btn4]

    for btn in buttons:
        btn.draw_button(window)

    longest_turn_text = scenario.get_longest_turn_text()
    turn_text = scenario.get_cur_turn_text()
    text_surf, _ = font.render(longest_turn_text, True, 'white')
    text_rect = text_surf.get_rect(topleft=(850, 60))
    pygame.draw.rect(window, 'black', text_rect)
    font.render_to(window, (850, 60), turn_text, 'white')

    return buttons


def run():
    pygame.init()
    window = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption('StormCell3')
    scenario = TheScenario()
    # font = pygame.freetype.Font("C:\\Users\\brend\\Documents\\StormCell\\stormCell3\\resources\\fonts\\vecna\\Vecna.otf", 12)
    font = pygame.freetype.SysFont('Verdana', 12)
    selected_node = None

    while True:  # main game loop
        buttons = draw_outliner(window, scenario, font, selected_node)

        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                for btn in buttons:
                    btn.click_test(mouse)

                new_selected_node = scenario.click_test(mouse)

                if new_selected_node is not None:
                    if selected_node is not None:
                        selected_node.undraw_as_selected(window)
                    selected_node = new_selected_node

        # TODO: Because things only happen on clicks, we *could* gate all refresh behind clicking
        for node in scenario.nodes:
            node.draw_connections(window)
        for node in scenario.nodes:
            node.draw_node(window, font)

        if selected_node is not None:
            selected_node.draw_as_selected(window)


        pygame.display.update()


if __name__ == '__main__':
    run()
