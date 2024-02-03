import os
from math import hypot
from pygame.font import get_default_font
from pygame.math import Vector3
import json

import pygame
import sys

from sc_ui.side_bar_state import SideBarState
from sc_game.game import Game
from sc_mapping.stormcell_map import MapOne
from sc_ui.side_bar import SideBar
from sc_game.military.mil_calc import test1


def get_neighbors(pos):
    return [
        (pos[0] - 1, pos[1]),
        (pos[0] + 1, pos[1]),
        (pos[0], pos[1] - 1),
        (pos[0], pos[1] + 1)
    ]


def lerp(v0, v1, t):
    return (1 - t) * v0 + t * v1


def is_black(color):
    return color[0] < 10 and color[1] < 10 and color[2] < 10

CLEAR_COLOR = "#80a8de"
SELECT_COLOR = "#ffee58"
OTHER_REGIONS_COLOR = "#00f2ff"

if __name__ == "__main__":
    pygame.init()
    size = (1100, 750)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption(f"Stormcell 4")
    screen.fill(CLEAR_COLOR)

    clock = pygame.time.Clock()

    the_map = MapOne((800, 750))
    the_ui = SideBar((800, 0), (300, 750))
    # for region in the_map.regions:
    #     region.draw(screen,"#D5CEAB",(50,50,50))

    starting_region = the_map.region_from_id("L25")
    starting_nation = the_map.nation_from_starting_region(starting_region)
    the_game = Game(starting_nation, the_map)

    print(starting_nation)

    # print(f"Army calc:{test1(the_map.active_nations[0],the_map.active_nations[1])}")

    the_map.color_according_to_ownership(screen)
    ui_state = SideBarState(None)
    the_ui.draw(screen, the_game, ui_state)
    # the_map.color_according_to_terrain(screen)

    the_map.draw_armies(screen)
    while True:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                clicked_region = the_map.region_clicked(pos)
                if clicked_region is not None:
                    clicked_region.draw(screen, None, SELECT_COLOR)
                    pygame.display.flip()

                    # the_widget = the_ui.get_selected_tile_widget()
                    # the_widget.txt = clicked_region.name
                    # the_widget.parent.update()
                    ui_state = SideBarState(clicked_region, True)
                    the_ui.draw(screen, the_game, ui_state)
                ui_state = SideBarState.glom([ui_state, the_ui.on_click(pos)])
                if ui_state.should_refresh:
                    screen.fill(CLEAR_COLOR)
                    the_map.color_according_to_ownership(screen)
                    the_map.draw_armies(screen)
                    if len(ui_state.other_regions)>0:
                        for region in ui_state.other_regions:
                            region.draw(screen, None, OTHER_REGIONS_COLOR)
                    ui_state.selected_region.draw(screen, None, SELECT_COLOR)
                    the_ui.draw(screen, the_game, ui_state)
        pygame.display.flip()

# if __name__ =="__main__":
#     pygame.init()
#     screen = pygame.display.set_mode((3000/4, 950))
#     tile_num=1
#     pygame.display.set_caption(f"L{tile_num}")
#     screen.fill((84, 186, 209))
#     imp = pygame.image.load("/Users/brendanritter/fun/StormCell/stormcell4/map.png").convert_alpha()
#     imp = pygame.transform.scale(imp, (3000/4,1000))
#     screen.blit(imp, (0, 0))
#
#     # paint screen one time
#     pygame.display.flip()
#     BLACK=(0,0,0,255)
#     PINK=(255,0,255)
#
#     tile_num_to_regions={}
#     region_lists=[]
#
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN and event.key==pygame.K_RETURN:
#                 tile_num_to_regions[tile_num] = region_lists
#                 tile_num+=1
#                 pygame.display.set_caption(f"L{tile_num}")
#                 region_lists = []
#             if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
#                 with open('region_list.txt',"w+") as f:
#                     f.write(json.dumps(tile_num_to_regions))
#             if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
#                 total_tile_num_to_regions={}
#                 for region_list_file in os.listdir("region_lists"):
#                     with open(f"region_lists/{region_list_file}") as f:
#                         for key, val in json.load(f).items():
#                             if val !=[]:
#                                 total_tile_num_to_regions[key]=val
#                 for i in range(86):
#                     herp=total_tile_num_to_regions.get(str(i),None)
#                     if herp is None:
#                         print(i)
#                 with open('region_list.txt', "w+") as f2:
#                     f2.write(json.dumps(total_tile_num_to_regions))
#
#             if event.type == pygame.MOUSEBUTTONUP:
#                 pos = pygame.mouse.get_pos()
#                 seen=set()
#                 fringe=[pos]
#                 finale=set()
#                 while len(fringe)>0:
#                     node=fringe.pop()
#                     #print(node)
#                     neighbors=get_neighbors(node)
#                     for neighbor in neighbors:
#                         if neighbor not in seen and neighbor not in finale:
#                             pixel=screen.get_at(neighbor)
#                             if is_black(pixel):
#                                 finale.add(neighbor)
#                             else:
#                                 #print(pixel)
#                                 fringe.append(neighbor)
#                     seen.add(node)
#
#                 node = finale.pop()
#                 ordered=[node]
#                 while len(finale)>0:
#                     closest_node=min(finale,key=lambda pt: hypot(pt[0]-node[0],pt[1]-node[1]))
#                     ordered.append(closest_node)
#                     node=closest_node
#                     finale.remove(closest_node)
#                 color_start = Vector3((255, 255, 255))
#                 color_end = Vector3((255, 255, 255))
#                 for i, pixel in enumerate(ordered):
#                     color=color_start.lerp(color_end,i/len(ordered))
#                     screen.set_at(pixel,color)
#                 pygame.display.flip()
#                 region_lists.append(ordered)
