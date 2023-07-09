import json

import pygame

from StormCell.stormcell4.sc_mapping.region_attrs import People, Culture, Religion, Region, Nation
from StormCell.stormcell4.sc_mapping.region_geometry import RegionGeometry


class MapOne(object):

    no_religion = Religion("R0")
    ice_spirits = Religion("Ice Spirits")
    hill_spirits = Religion("Hill Spirits")
    barrow_worship = Religion("Barrows")
    imperial_cult = Religion("Imperial Cult")
    water_gods = Religion("Water Gods")
    deep_gods = Religion("Deep Gods")
    earth_gods = Religion("Earth Gods")

    NP = Culture("Northern Plains", "NP")
    HL = Culture("Hillsland", "HL")
    IMP = Culture("Imperial", "IMP")
    SI = Culture("Southern Isles", "SI")
    WD = Culture("Great Woods", "WD")
    PA = Culture("Peripa","PA")
    NA = Culture("None","NA")

    fartheners = People(
        name="fartheners",
        culture=NP,
        religion=ice_spirits,
        ebang=.1,
        magic=0,
        religiousness=.3,
        tradition=.7
    )
    raiders = People(
        name="raiders",
        culture=NP,
        religion=Religion("R0"),
        ebang=.5,
        magic=.1,
        religiousness=.2,
        tradition=.3
    )
    northumberland = People(
        name="northumberlanders",
        culture=HL,
        religion=ice_spirits,
        ebang=.4,
        magic=.1,
        religiousness=.3,
        tradition=.4,
    )
    druids = People(
        name="druids",
        culture=HL,
        religion=hill_spirits,
        ebang=.1,
        magic=.7,
        religiousness=.7,
        tradition=.7
    )
    barrowdwellers = People(
        name="barrowdwellers",
        culture=HL,
        religion=barrow_worship,
        ebang=.1,
        magic=.3,
        religiousness=.4,
        tradition=.9
    )
    imperial = People(
        name="imperial",
        culture=IMP,
        religion=imperial_cult,
        ebang=.6,
        magic=.1,
        religiousness=.2,
        tradition=.3
    )
    islanders = People(
        name="islanders",
        culture=SI,
        religion=water_gods,
        ebang=.4,
        magic=.3,
        religiousness=.2,
        tradition=.1
    )
    deepseekers = People(
        name="deepseekers",
        culture=SI,
        religion=deep_gods,
        ebang=.2,
        magic=.5,
        religiousness=.8,
        tradition=.9,
    )
    peripa = People(
        name="peripa",
        culture=PA,
        religion=no_religion,
        ebang=.6,
        magic=.3,
        religiousness=0,
        tradition=.6,
    )
    lone_tower = People(
        name="loner",
        culture=NA,
        religion=no_religion,
        ebang=.5,
        magic=1,
        religiousness=.1,
        tradition=.6,
    )
    haverguard = People(
        name="haverguard",
        culture=WD,
        religion=earth_gods,
        ebang=.4,
        magic=.3,
        religiousness=.3,
        tradition=.5
    )
    selucians = People(
        name="selucians",
        culture=WD,
        religion=earth_gods,
        ebang=.1,
        magic=.5,
        religiousness=.7,
        tradition=.5,
    )

    def __init__(self):

        self.peoples = [
            MapOne.fartheners,
            MapOne.raiders,
            MapOne.northumberland,
            MapOne.druids,
            MapOne.barrowdwellers,
            MapOne.imperial,
            MapOne.islanders,
            MapOne.deepseekers,
            MapOne.peripa,
            MapOne.lone_tower,
            MapOne.haverguard,
            MapOne.selucians
        ]
        self.cultures=[
            MapOne.NP,
            MapOne.HL,
            MapOne.IMP,
            MapOne.SI,
            MapOne.WD,
            MapOne.PA,
            MapOne.NA
        ]
        self.religions=[
            MapOne.no_religion,
            MapOne.ice_spirits,
            MapOne.hill_spirits,
            MapOne.barrow_worship,
            MapOne.imperial_cult,
            MapOne.water_gods,
            MapOne.deep_gods,
            MapOne.earth_gods,
        ]


        L1 = Region("L1")
        L2 = Region("L2")
        L3 = Region("L3")
        L4 = Region("L4")
        L5 = Region("L5")
        L6 = Region("L6")
        L7 = Region("L7")
        L8 = Region("L8")
        L9 = Region("L9")
        L10 = Region("L10")
        L11 = Region("L11")
        L12 = Region("L12")
        L13 = Region("L13")
        L14 = Region("L14")
        L15 = Region("L15")
        L16 = Region("L16")
        L17 = Region("L17")
        L18 = Region("L18")
        L19 = Region("L19")
        L20 = Region("L20")
        L21 = Region("L21")
        L22 = Region("L22")
        L23 = Region("L23")
        L24 = Region("L24")
        L25 = Region("L25")
        L26 = Region("L26")
        L27 = Region("L27")
        L28 = Region("L28")
        L29 = Region("L29")
        L30 = Region("L30")
        L31 = Region("L31")
        L32 = Region("L32")
        L33 = Region("L33")
        L34 = Region("L34")
        L35 = Region("L35")
        L36 = Region("L36")
        L37 = Region("L37")
        L38 = Region("L38")
        L39 = Region("L39")
        L40 = Region("L40")
        L41 = Region("L41")
        L42 = Region("L42")
        L43 = Region("L43")
        L44 = Region("L44")
        L45 = Region("L45")
        L46 = Region("L46")
        L47 = Region("L47")
        L48 = Region("L48")
        L49 = Region("L49")
        L50 = Region("L50")
        L51 = Region("L51")
        L52 = Region("L52")
        L53 = Region("L53")
        L54 = Region("L54")
        L55 = Region("L55")
        L56 = Region("L56")
        L57 = Region("L57")
        L58 = Region("L58")
        L59 = Region("L59")
        L60 = Region("L60")
        L61 = Region("L61")
        L62 = Region("L62")
        L63 = Region("L63")
        L64 = Region("L64")
        L65 = Region("L65")
        L66 = Region("L66")
        L67 = Region("L67")
        L68 = Region("L68")
        L69 = Region("L69")
        L70 = Region("L70")
        L71 = Region("L71")
        L72 = Region("L72")
        L73 = Region("L73")
        L74 = Region("L74")
        L75 = Region("L75")
        L76 = Region("L76")
        L77 = Region("L77")
        L78 = Region("L78")
        L79 = Region("L79")
        L80 = Region("L80")
        L81 = Region("L81")
        L82 = Region("L82")
        L83 = Region("L83")
        L84 = Region("L84")
        L85 = Region("L85")

        farthener_tribes = Nation("Farthener Tribes",None,None,None)
        dunhollow_tribes = Nation("Dunhollow Tribes",None,None,None)
        amonhold = Nation("Amonhold",None,None,None)
        pinemar_keep = Nation("Pinemorn",None,None,None)
        tower_of_illedion=Nation("Illedion's Tower",None,None,None)
        tower_of_eregion=Nation("Eregion's Tower",None,None,None)
        zultans_keep = Nation("Zultan's Keep",None,None,None)
        artemons_hold = Nation("Artemon's Hold",None,None,None)
        jibacoa = Nation("Jibacoa",None,None,None)
        maniabon = Nation("Maniabon",None,None,None)
        canimao = Nation("Canimao",None,None,None)
        naguabo = Nation("Naguabo",None,None,None)
        seluceria = Nation("Seluceria",None,None,None)
        havernia = Nation("Havernia",None,None,None)
        iphakhealis = Nation("Iphakhealis' Hold",None,None,None)
        northumber = Nation("Northumber",None,None,None)
        central_empire = Nation("Central Empire",None,None,None)
        north_east_empire = Nation("North East Empire",None,None,None)
        north_west_empire = Nation("North West Empire",None,None,None)
        south_west_empire = Nation("South West Empire",None,None,None)
        south_east_empire = Nation("South East Empire",None,None,None)


        self.national_colors = {
            farthener_tribes: "#0064ff",
            dunhollow_tribes: "#6a472f",
            amonhold: "#c75700",
            pinemar_keep: "#705700",
            tower_of_illedion: "#9e0095",
            tower_of_eregion: "#69008b",
            artemons_hold: "#781de7",
            zultans_keep: "#7a3a8f",
            jibacoa: "#3bf9f3",
            maniabon: "#24a09c",
            canimao: "#24a072",
            naguabo: "#00f9be",
            seluceria: "#004022",
            havernia: "#029900",
            iphakhealis: "#9e00ff",
            northumber: "#002f55",
            central_empire: "#ff0011",
            north_east_empire: "#bc000d",
            north_west_empire: "#820009",
            south_west_empire: "#ff545f",
            south_east_empire: "#ac3b42",
        }

        #guohugong = Nation("Guohugong")
        #huangshagong = Nation("Huangshagong")
        #coastal_hill_palace = Nation("Coastal Hill Palace") #shanhaiangong
        #celestial_palace = Nation("Celestial Palace") #zhizunxiangong

        self.starting_regions = {
            farthener_tribes:[L1,L2,L3,L4], #A
            dunhollow_tribes:[L6,L7,L8], #D
            amonhold:[L5,L15,L16], #B
            pinemar_keep:[L17,L18,L20,L19,L21], #C
            tower_of_eregion:[L85], #E
            tower_of_illedion:[L78], #F
            artemons_hold:[L13],
            zultans_keep:[L79,L80], #G
            jibacoa:[L82], #H
            canimao:[L81], #I
            maniabon:[L59,L84,L65], #J
            naguabo:[L62,L60,L61,L63,L66], #K
            seluceria:[L56,L57,L54,L58,L68], #L
            havernia:[L48,L83,L49,L51], #M
            iphakhealis:[L45,L43], #N
            northumber:[L71,L72,L73,L77,L76,L74,L75], #O
            central_empire:[L28,L32,L33,L34], #Q
            south_east_empire:[L38,L39,L47], #T
            south_west_empire:[L26,L35,L36,L37], #S
            north_west_empire:[L10,L9,L12,L11], #R
            north_east_empire:[L25,L27,L29,L30,L31,L70,L69],#P
        }



        self.color_mapping={
            "ff0000":L1,
            "2500ff":L2,
            "eb00ff":L3,
            "66dd71":L4,
            "66b9dd":L5,
            "ddae66":L6,
            "5f00e4":L7,
            "016400":L8,
            "8cfff0":L9,
            "6b0082":L10,
            "ffac00":L11,
            "a00000":L12,
            "45784c":L13,
            "764578":L14,
            "d0869f":L15,
            "988f01":L16,
            "03ff00":L17,
            "273a9e":L18,
            "ccce00":L19,
            "fea3ff":L20,
            "d3d3d3":L21,
            "2c2c2c":L22,
            "602929":L23,
            "295960":L25,
            "007587":L26,
            "197528":L27,
            "7e0080":L28,
            "2f3c99":L29,
            "157e2d":L30,
            "aa0839":L31,
            "7b7b7b":L32,
            "ba1d62":L33,
            "1d60ba":L34,
            "803c00":L35,
            "a5a5a5":L36,
            "500000":L37,
            "4fa248":L38,
            "fff69a":L39,
            "ff4f4f":L40,
            "4f9aff":L41,
            "9857a6":L42,
            "d55e00":L43,
            "2c5e00":L45,
            "434343":L47,
            "00044f":L48,
            "ddcf41":L49,
            "91882c":L50,
            "ffe800":L51,
            "757148":L52,
            "4a4616":L53,
            "464430":L54,
            "baad23":L55,
            "363200":L56,
            "ffd55c":L57,
            "ffaf5c":L58,
            "6c30c0":L59,
            "542695":L60,
            "6e578f":L61,
            "9575c1":L62,
            "757cc1":L63,
            "404cc0":L65,
            "1723a2":L66,
            "0c605d":L67,
            "003635":L68,
            "1a8e8a":L69,
            "1dc1bc":L70,
            "20efe8":L71,
            "486463":L72,
            "6a9896":L73,
            "6edaa7":L74,
            "4dffab":L75,
            "0bbc68":L76,
            "048c4c":L77,
            "2a362a":L78,
            "016636":L79,
            "004022":L80,
            "c03065":L81,
            "c17e97":L82,
            "ff9dc1":L83,
            "7b002d":L84,
            "996c27":L85,

        }

        self.region_graph=[
            (L1,L2),
            (L3,L2),
            (L3,L4),
            (L4,L7),
            (L4,L6),
            (L4,L5),
            (L8,L7),
            (L7,L6),
            (L6,L5),
            (L8,L10),
            (L10,L7),
            (L10,L9),
            (L7,L9),
            (L9,L13),
            (L9,L12),
            (L5,L15),
            (L5,L16),
            (L5,L14),
            (L6,L13),
            (L13,L14),
            (L17,L15),
            (L17,L16),
            (L15,L16),
            (L16,L15),
            (L16,L14),
            (L10,L11),
            (L11,L9),
            (L11,L28),
            (L11,L26),
            (L28,L12),
            (L12,L25),
            (L13,L25),
            (L14,L25),
            (L26,L28),
            (L28,L32),
            (L12,L32),
            (L32,L27),
            (L25,L27),
            (L27,L29),
            (L25,L29),
            (L14,L29),
            (L17,L20),
            (L17,L18),
            (L17,L19),
            (L20,L18),
            (L18,L19),
            (L20,L19),
            (L20,L21),
            (L21,L19),
            (L16,L22),
            (L19,L22),
            (L19,L23),
            (L22,L23),
            (L22,L29),
            (L23,L30),
            (L29,L30),
            (L29,L31),
            (L30,L31),
            (L30,L70),
            (L31,L69),
            (L31,L70),
            (L70,L69),
            (L70,L71),
            (L69,L71),
            (L71,L73),
            (L73,L72),
            (L71,L72),
            (L73,L74),
            (L72,L77),
            (L73,L77),
            (L73,L76),
            (L74,L76),
            (L73,L75),
            (L76,L75),
            (L77,L75),
            (L26,L35),
            (L35,L37),
            (L28,L37),
            (L32,L33),
            (L28,L33),
            (L33,L38),
            (L34,L33),
            (L34,L38),
            (L37,L38),
            (L36,L37),
            (L35,L36),
            (L36,L41),
            (L36,L40),
            (L37,L41),
            (L40,L41),
            (L39,L34),
            (L38,L39),
            (L37,L42),
            (L38,L42),
            (L43,L42),
            (L41,L45),
            (L45,L43),
            (L41,L43),
            (L39,L47),
            (L39,L50),
            (L39,L48),
            (L42,L48),
            (L83,L43),
            (L83,L48),
            (L43,L48),
            (L43,L83),
            (L48,L50),
            (L48,L49),
            (L83,L49),
            (L49,L50),
            (L50,L47),
            (L49,L51),
            (L50,L51),
            (L51,L52),
            (L50,L52),
            (L47,L52),
            (L47,L58),
            (L52,L54),
            (L51,L53),
            (L53,L55),
            (L51,L55),
            (L55,L54),
            (L52,L55),
            (L58,L54),
            (L58,L57),
            (L54,L57),
            (L54,L56),
            (L55,L56),
            (L53,L56),
            (L53,L57),
            (L56,L57),
            (L84,L62),
            (L84,L60),
            (L84,L61),
            (L62,L60),
            (L60,L61),
            (L62,L63),
            (L60,L63),
            (L61,L63),
            (L67,L68),
            (L79,L80),
            (L78,L85),
            (L31,L47)
        ]

        self.load_and_connect_polys()

    @property
    def regions(self):
         return list(self.color_mapping.values())


    def load_and_connect_polys(self):
        with open('region_list.txt', "r") as f:
            regions_dict = json.load(f)
        for region in self.regions:
            region.geometry=RegionGeometry(
                regions_dict.get(str(region.tile_num),[])
            )

    def region_clicked(self,click_pos):
        for region in self.regions:
            if region.geometry.in_bbox(click_pos) and region.geometry.in_polys(click_pos):
                return region
        return None

    def reverse_color_mapping(self):
        return {region.tile_num:color for color,region in self.color_mapping.items()}

    @staticmethod
    def l_val(hex_color):
        pycolor=pygame.Color(hex_color)
        color=(pycolor.r/255.0,pycolor.g/255.0,pycolor.b/255.0)
        c_max=max(color)
        c_min=min(color)
        return ((c_max+c_min)/2)*100

    def color_according_to_ownership(self,screen):
        unseen_regions=set(self.regions)
        # print(unseen_regions)
        for nation,regions in self.starting_regions.items():
            for region in regions:
                try:
                    unseen_regions.remove(region)
                    fill_color=self.national_colors[nation]
                    edge_color_to_use = (200,200,200) if MapOne.l_val(fill_color) <=20 else (50,50,50)
                    if region.tile_num == 73:
                        print(MapOne.l_val(fill_color))
                    region.draw(screen, fill_color=fill_color, edge_color=edge_color_to_use)
                except KeyError as e:
                    print(region.tile_num)
        for unseen_region in unseen_regions:
            unseen_region.draw(screen, fill_color="#D5CEAB", edge_color=(50, 50, 50))

