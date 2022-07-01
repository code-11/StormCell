import pygame, sys
from pygame.locals import *


def auto_text(text_id, window, text_save_map, font, new_text, loc):
    old_text = text_save_map.get(text_id, '')
    larger_text = new_text if len(new_text) >= len(old_text) else old_text

    old_text_surf, _ = font.render(old_text, True, 'white')
    old_text_rect = old_text_surf.get_rect(topleft=loc)

    text_surf, _ = font.render(larger_text, True, 'white')
    text_rect = text_surf.get_rect(topleft=loc)

    largest_width = max(text_rect.width, old_text_rect.height)
    largest_height = max(text_rect.height, old_text_rect.height)
    largest_rect = Rect(loc[0], loc[1], largest_width, largest_height)
    pygame.draw.rect(window, 'black', largest_rect)

    font.render_to(window, loc, new_text, 'white')
    text_save_map[text_id] = new_text