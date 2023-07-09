import os
from math import hypot
from pygame.math import Vector3
import json

import pygame
import sys

from StormCell.stormcell4.sc_mapping.stormcell_map import MapOne



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
    screen = pygame.display.set_mode((3000/4, 950))
    pygame.display.set_caption(f"Stormcell 4")
    screen.fill("#80a8de")

    the_map=MapOne()

    # for region in the_map.regions:
    #     region.draw(screen,"#D5CEAB",(50,50,50))
    the_map.color_according_to_ownership(screen)
    pygame.display.flip()

    while True:
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




