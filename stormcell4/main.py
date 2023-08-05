import os
from math import hypot
from pygame.math import Vector3
import json

import pygame
import sys

from StormCell.stormcell4.sc_game.game import Game
from StormCell.stormcell4.sc_mapping.stormcell_map import MapOne
from StormCell.stormcell4.sc_ui.side_bar import SideBar

import pygame_gui


def get_neighbors(pos):
    return [
        (pos[0]-1,pos[1]),
        (pos[0]+1,pos[1]),
        (pos[0],pos[1]-1),
        (pos[0],pos[1]+1)
    ]

def lerp(v0, v1, t):
    return (1 - t) * v0 + t * v1

def is_black(color):
    return color[0]<10 and color[1]<10 and color[2]<10

if __name__ == "__main__":
    pygame.init()
    size=(1100, 950)
    screen = pygame.display.set_mode(size)
    manager = pygame_gui.UIManager(size)

    pygame.display.set_caption(f"Stormcell 4")
    screen.fill("#80a8de")

    clock = pygame.time.Clock()

    the_map=MapOne()
    the_ui = SideBar((800,0),(300,950))
    # for region in the_map.regions:
    #     region.draw(screen,"#D5CEAB",(50,50,50))

    starting_region=the_map.region_from_id("L28")
    starting_nation=the_map.nation_from_starting_region(starting_region)
    the_game = Game(starting_nation)

    print(starting_nation)

    the_map.color_according_to_ownership(screen)
    the_ui.draw(screen, the_game)
    # the_map.color_according_to_terrain(screen)

    button_layout_rect = pygame.Rect(800, 0, 100, 50)
    hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((800,0), (100, 50)),
                                                text='Say Hello',
                                                manager=manager)

    while True:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                clicked_region=the_map.region_clicked(pos)
                if clicked_region is not None:
                    clicked_region.draw(screen,(255,0,0),(50,50,50))
                    pygame.display.flip()
            manager.process_events(event)
        manager.update(time_delta)
        manager.draw_ui(screen)
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




