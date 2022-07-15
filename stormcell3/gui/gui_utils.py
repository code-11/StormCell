import pygame, sys
from pygame.locals import *


def auto_text(text_id, window, text_save_map, font, new_text, loc, text_color='white', background_color='black'):
    old_text = text_save_map.get(text_id, '')
    larger_text = new_text if len(new_text) >= len(old_text) else old_text

    old_text_surf, _ = font.render(old_text, True, text_color)
    old_text_rect = old_text_surf.get_rect(topleft=loc)

    text_surf, _ = font.render(larger_text, True, text_color)
    text_rect = text_surf.get_rect(topleft=loc)

    largest_width = max(text_rect.width, old_text_rect.width)
    largest_height = max(text_rect.height, old_text_rect.height)
    largest_rect = Rect(loc[0], loc[1], largest_width, largest_height)
    pygame.draw.rect(window, background_color, largest_rect)

    font.render_to(window, loc, new_text, text_color)
    text_save_map[text_id] = new_text

    return largest_width, largest_height