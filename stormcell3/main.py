import pygame, sys
from pygame.locals import *
from scbutton import SCButton
from Scenarios.test_scenario import TestScenario


def draw_outliner(window, turn, buttons, font):
    pygame.draw.line(window, 'white', (800, 0), (800, 600))
    for btn in buttons:
        btn.draw_button(window)

    text_surf, _ = font.render(f"Turn: {turn}", True, 'white')
    text_rect = text_surf.get_rect(topleft=(850, 60))
    pygame.draw.rect(window,'black', text_rect)
    font.render_to(window, (850, 60), f"Turn: {turn}", (254, 254, 254))


def run():
    pygame.init()
    window = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption('StormCell3')
    scenario = TestScenario()
    # font = pygame.freetype.Font("C:\\Users\\brend\\Documents\\StormCell\\stormCell3\\resources\\fonts\\vecna\\Vecna.otf", 12)
    font = pygame.freetype.SysFont('Verdana', 12)

    btn1 = SCButton(Rect(800, 540, 200, 60), font, 'Next Turn')
    btn1.on_click = scenario.incr_turn
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
            node.draw_node(window, font)
        draw_outliner(window, scenario.turn, buttons, font)
        pygame.display.update()


if __name__ == '__main__':
    run()
