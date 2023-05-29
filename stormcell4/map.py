from main import People, Culture, Religion, Region, Nation


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

        farthener_tribes = Nation("Farthener Tribes")
        dunhollow_tribes = Nation("Dunhollow Tribes")
        amonhold = Nation("Amonhold")
        pinemar_keep = Nation("Pinemorn")
        tower_of_illedion=Nation("Illedion's Tower")
        tower_of_eregion=Nation("Eregion's Tower")
        zultans_keep = Nation("Zultan's Keep")
        jibacoa = Nation("Jibacoa")
        maniabon = Nation("Maniabon")
        canimao = Nation("Canimao")
        naguabo = Nation("Naguabo")
        seluceria = Nation("Seluceria")
        havernia = Nation("Havernia")
        iphakhealis = Nation("Iphakhealis' Hold")
        northumber = Nation("Northumber")
        #guohugong = Nation("Guohugong")
        #huangshagong = Nation("Huangshagong")
        coastal_hill_palace = Nation("Coastal Hill Palace") #shanhaiangong
        celestial_palace = Nation("Celestial Palace") #zhizunxiangong

        self.starting_regions = {
            farthener_tribes:[L1,L2,L3,L4],
            dunhollow_tribes:[L6,L7,L8],
            amonhold:[L5,L15,L16],
            pinemar_keep:[L17,L18,L20,L19,L21],
            tower_of_eregion:[L81],
            tower_of_illedion:[L78],
            zultans_keep:[L79,L80],
            jibacoa:[L82],
            canimao:[L81],
            maniabon:[L59,L84,L65],
            naguabo:[L62,L60,L61,L63,L66],
            seluceria:[L56,L57,L54,L58,L68],
            havernia:[L48,L83,L49,L51],
            iphakhealis:[L45,L43],
            northumber:[L71,L72,L72,L77,L76,L74,L75],
            guohugong:[L38,L39,L47]
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
            (L78,L81),
            (L31,L47)
        ]



