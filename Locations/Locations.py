"""
All hardcoded pixel locations are going to live here.
In the event a pixel location needs to change, it changes here.
"""

# reactor power
REACTOR_SEGMENTS = [ (1484, 45) , (1464, 45) , (1444, 45) , (1424, 45) , (1404, 45) , (1384, 45) , (1364, 45) , (1344, 45) ]

# hull health
PLAYER_HULL_SEGMENTS = [ (128, 33)
, (128, 57)
, (128, 81)
, (128, 105)
, (128, 129)
, (128, 153)
, (128, 177)
, (128, 201)
, (128, 225)
, (128, 249)
, (128, 273)
, (128, 297)
, (128, 321)
, (128, 345)
, (128, 369)
, (128, 393)
, (128, 417)
, (128, 441)
, (128, 465)
, (128, 489)
, (128, 513)
, (128, 537)
, (128, 561)
, (128, 585)
, (128, 609)
, (128, 633)
, (128, 657)
, (128, 681)
, (128, 705)
, (128, 729)
]

ENEMY_HULL_SEGMENTS = [ (255, 1578)
, (255, 1600)
, (255, 1622)
, (255, 1644)
, (255, 1666)
, (255, 1688)
, (255, 1710)
, (255, 1732)
, (255, 1754)
, (255, 1776)
, (255, 1798)
, (255, 1820)
, (255, 1842)
, (255, 1864)
, (255, 1886)
, (255, 1908)
, (255, 1930)
, (255, 1952)
, (255, 1974)
, (255, 1996)
]


# power/health of all major systems
SHIELD_SEGMENTS = [
[ (1430, 165) ,
(1430, 168) ,
(1430, 171) ,
(1430, 174) ,
(1430, 177) ,
(1430, 180) ,
(1430, 183) ,
(1430, 186) ,
(1430, 189) ,
(1430, 192) ]
,
[ (1414, 165) ,
(1414, 168) ,
(1414, 171) ,
(1414, 174) ,
(1414, 177) ,
(1414, 180) ,
(1414, 183) ,
(1414, 186) ,
(1414, 189) ,
(1414, 192) ]
]
ENGINE_SEGMENTS = [
[ (1430, 238) ,
(1430, 241) ,
(1430, 244) ,
(1430, 247) ,
(1430, 250) ,
(1430, 253) ,
(1430, 256) ,
(1430, 259) ,
(1430, 262) ,
(1430, 265) ]
,
[ (1414, 238) ,
(1414, 241) ,
(1414, 244) ,
(1414, 247) ,
(1414, 250) ,
(1414, 253) ,
(1414, 256) ,
(1414, 259) ,
(1414, 262) ,
(1414, 265) ]
]
MEDBAY_SEGMENTS = [
[ (1430, 311) ,
(1430, 314) ,
(1430, 317) ,
(1430, 320) ,
(1430, 323) ,
(1430, 326) ,
(1430, 329) ,
(1430, 332) ,
(1430, 335) ,
(1430, 338) ]
]
OXYGEN_SEGMENTS = [
[ (1430, 384) ,
(1430, 387) ,
(1430, 390) ,
(1430, 393) ,
(1430, 396) ,
(1430, 399) ,
(1430, 402) ,
(1430, 405) ,
(1430, 408) ,
(1430, 411) ]
]
WEAPON_SEGMENTS = [
[ (1430, 457) ,
(1430, 460) ,
(1430, 463) ,
(1430, 466) ,
(1430, 469) ,
(1430, 472) ,
(1430, 475) ,
(1430, 478) ,
(1430, 481) ,
(1430, 484) ]
,
[ (1414, 457) ,
(1414, 460) ,
(1414, 463) ,
(1414, 466) ,
(1414, 469) ,
(1414, 472) ,
(1414, 475) ,
(1414, 478) ,
(1414, 481) ,
(1414, 484) ]
,
[ (1398, 457) ,
(1398, 460) ,
(1398, 463) ,
(1398, 466) ,
(1398, 469) ,
(1398, 472) ,
(1398, 475) ,
(1398, 478) ,
(1398, 481) ,
(1398, 484) ]
]

# pixel locations for the specific weapons
BURST_LASER = [(1424, 592)]
ARTEMIS = [(1423, 784)]

# shield bubbles
PLAYER_BUBBLES = [
(228, 52)
, (228, 98)
, (228, 144)
, (228, 190)
]
ENEMY_BUBBLES = [
(321, 1668)
, (321, 1704)
, (321, 1740)
, (321, 1776)
, (321, 1812)
, (321, 1848)
, (321, 1884)
, (321, 1920)
, (321, 1956)
, (321, 1992)
]

# rooms on the Kestrel
# doors on the Kestrel
ROOMS = [
            (-1, 1),      # special one for space
            (772 ,543),  # row col for engine room
            (666, 543),  # row col for oxygen room
            (759, 756),  # row col for weapons room
            (846, 1038), # row col for shields room
            (696, 1037), # row col for medbay room
            #12 non essential rooms here
            (769, 434), (659, 681), (875, 541),(878, 676),
            (582, 892), (695, 892),(841, 892), (952, 892),
            (738, 1178), (809, 1178), (776, 1312), (776, 1418)
        ]
DOORS = [
            (739, 402), (741, 472), (696, 571), (654, 613), (697, 712),
            (839, 581), (872, 612), (839, 713), (736, 824), (801, 825),
            (549, 864), (620, 924), (655, 964), (985, 863), (913, 924),
            (872, 964), (769, 993), (724, 1105), (796,1105),(726, 1246),
            (801, 1246), (800, 1384)
        ]


# enemy ship title (row, col, width, height)
# this gives the top right corner, then width going to the left and height going down.
ENEMY_TITLE = [223, 2515, 285, 28]