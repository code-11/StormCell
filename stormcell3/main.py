import pygame, sys
from pygame.locals import *
from node import Node
from scbutton import SCButton
from Scenarios.testscenario import TestScenario

def draw_outliner(window, turn, buttons, font):
    pygame.draw.line(window, 'white', (800, 0), (800, 600))
    for btn in buttons:
        btn.draw_button(window)

    font.render_to(window, (850,  60), f"Turn: {turn}", (254, 254, 254))


def incr_turn(turn, nations):
    major_turn, nation_index = turn
    if nation_index-1 == nations:
        return major_turn+1, 0
    else:
        return major_turn, nation_index + 1

def run():
    pygame.init()
    window = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption('StormCell3')
    scenario = TestScenario()
    turn = (0, 0)
    # font = pygame.freetype.Font("C:\\Users\\brend\\Documents\\StormCell\\stormCell3\\resources\\fonts\\vecna\\Vecna.otf", 12)
    font = pygame.freetype.SysFont('Verdana', 12)

    btn1 = SCButton(Rect(800, 540, 200, 60), font, 'Next Turn')
    buttons = [btn1]

    while True:  # main game loop
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                for btn in buttons:
                    btn.click_test(mouse)

        for node in scenario.nodes:
            node.draw_connections(window)
        for node in scenario.nodes:
            node.draw_node(window)
        draw_outliner(window, turn, buttons, font)
        pygame.display.update()


if __name__ == '__main__':
    run()
