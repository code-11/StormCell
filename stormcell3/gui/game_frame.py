import pygame
from pygame.rect import Rect

from Scenarios.scenario import Scenario
from gui.frame import Frame
from gui.gui_utils import auto_text
import gui.menu_frame
from gui.scbutton import SCButton


class GameFrame(Frame):

    def __init__(self, window, frame_changer, scenario):
        super().__init__(window, frame_changer)
        self.scenario = scenario
        self.selected_node = None
        self.end_btn = None
        self.confirm_save_btn = None

    def pre_event_draw(self):
        self.buttons = self.draw_outliner(self.window, self.scenario, self.default_font, self.selected_node, self.text_save_map)

        if self.scenario.winning_nation is not None:
            winning_text = f" {self.scenario.winning_nation.name} has won! \n (Click here to exit) "
            end_btn = SCButton('end-btn', pygame.Rect(500, 300, 200, 60), self.default_font, winning_text, text_color='black',
                               background_color='white')
            end_btn.on_click = self.exit_to_menu
            self.buttons.clear()
            self.buttons.append(end_btn)
            self.end_btn = end_btn

    def on_left_click(self, mouse):
        super().on_left_click(mouse)
        if self.confirm_save_btn is not None:
            self.confirm_save_btn.click_test(mouse)

        new_selected_node = self.scenario.click_test(mouse)

        if new_selected_node is not None:
            if self.selected_node is not None:
                self.selected_node.undraw_as_selected(self.window)
            self.selected_node = new_selected_node

    def on_right_click(self, mouse):
        if self.selected_node is not None:
            destination_node = self.scenario.click_test(mouse)
            self.scenario.move_command(self.selected_node, destination_node)

    def post_event_draw(self):
        # TODO: Because things only happen on clicks, we *could* gate all refresh behind clicking
        for node in self.scenario.nodes:
            node.draw_connections(self.window)
        for node in self.scenario.nodes:
            node.draw_node(self.window, self.default_font)

        if self.selected_node is not None:
            self.selected_node.draw_as_selected(self.window)

        if self.end_btn is not None:
            self.end_btn.draw_button(self.window, self.text_save_map)

        if self.confirm_save_btn is not None:
            self.confirm_save_btn.draw_button(self.window, self.text_save_map)

    def change_frame_to_menu(self):
        frame = gui.menu_frame.MenuFrame(self.window, self.frame_changer)
        self.frame_changer(frame)

    def confirm_save(self):
        confirm_save_text = "Sucessfully Saved \n (Click here to exit) "
        confirm_btn = SCButton('confirm-save-btn', pygame.Rect(500, 300, 200, 60), self.default_font, confirm_save_text,
                           text_color='black',
                           background_color='white')
        this = self
        def on_confirm():
            this.confirm_save_btn = None
            confirm_btn.undraw_button(this.window, background_override='black')

        confirm_btn.on_click = on_confirm
        confirm_btn.draw_button(self.window, self.text_save_map)
        self.confirm_save_btn = confirm_btn

    def save_scenario(self):
        Scenario.save_scenario(self.scenario)
        self.confirm_save()

    def draw_outliner(self, window, scenario, font, selected_node, text_save_map):
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

        btn5 = SCButton('next-turn', Rect(800, 510, 200, 60), font, 'Next Turn')
        btn5.on_click = scenario.incr_turn_and_check_for_end

        btn6 = SCButton('save', Rect(800, 570, 100, 30), font, 'Save')
        btn6.on_click = self.save_scenario

        btn7 = SCButton('exit', Rect(900, 570, 100, 30), font, 'Exit')
        btn7.on_click = self.change_frame_to_menu

        buttons = [btn1, btn2, btn3, btn4, btn5, btn6, btn7]

        for btn in buttons:
            btn.draw_button(window, text_save_map)

        return buttons

