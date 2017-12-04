"""
File to generate location code for some of the locations module
Just so I don't have to retype all of them if it changes
"""

"""
Generate location list for reactor segments
@:param starting row of first segment (lowest on the screen)
@:param col of the segments
@:param row height: number of pixels between segments on the y axis
"""
def generate_reactor_segments(starting_row, col, row_height):
    num_segments = 8 # default to 8 before you upgrade the ship
    row = starting_row
    print "REACTOR_SEGMENTS = ["
    for i in range(num_segments):
        print "(" + str(row) + ", " + str(col) + ")"
        if i < num_segments - 1:
            print ",",
        row -= row_height
    print "]"

"""
Generate list of all player hull segments
@:param row of all health segments
@:param col: starting column of first segment
@:param col_width: distance between health segments on the x axis
"""
def generate_player_hull_segments(row, starting_col, col_width):
    num_segments = 30  # 30 hull segments
    col = starting_col
    print "PLAYER_HULL_SEGMENTS = [",
    for i in range(num_segments):
        print "(" + str(row) + ", " + str(col) + ")"
        if i < num_segments - 1:
            print ",",
        col += col_width
    print "]"

"""
Generate list of all enemy hull segments (20)
@:param row of all health segments
@:param col: starting column of first segment
@:param col_width: distance between health segments on the x axis
"""
def generate_enemy_hull_segments(row, starting_col, col_width):
    num_segments = 20  # 20 hull segments
    col = starting_col
    print "ENEMY_HULL_SEGMENTS = [",
    for i in range(num_segments):
        print "(" + str(row) + ", " + str(col) + ")"
        if i < num_segments - 1:
            print ",",
        col += col_width
    print "]"

"""
Generate segment locations for all major systems. Shields, engines, medbay, O2, and weapons
@:param starting row of lowest segment
@:param starting col of leftmost system
@:param row_height distance between rows
@:param col_width distance between columns
@:param seg_height height of segments
@:param seg_width width of segments
"""
def generate_system_segments(starting_row, starting_col, row_height, col_width, seg_height, seg_width):
    num_shield_segments = 2
    num_engine_segments = 2
    num_medbay_segments = 1
    num_oxygen_segments = 1
    num_weapon_segments = 3
    segments = [num_shield_segments, num_engine_segments, num_medbay_segments, num_oxygen_segments, num_weapon_segments]
    titles = ["SHIELD_SEGMENTS", "ENGINE_SEGMENTS", "MEDBAY_SEGMENTS", "OXYGEN_SEGMENTS", "WEAPON_SEGMENTS"]
    col = starting_col
    for i in range (len(titles)):
        system = titles[i]
        print system + " = ["
        row = starting_row
        num_segments = segments[i]
        for j in range (num_segments):
            print "[",
            #generate 10 pixel locations across the segment
            pix_width = seg_width / 10
            pix_row = row
            pix_col = col
            for k in range(10):
                print "(" + str(pix_row) + ", " + str(pix_col) + ")",
                if k < 9:
                    print ","
                pix_col += pix_width
            row -= row_height
            print "] "
            if j < num_segments - 1:
                print ", "
        col += col_width
        print "]"

"""
generate location list of player's shield bubbles
@:param row of shield bubbles
@:param starting_col of shield bubbles
@:param col_width distance between shield bubble segments
"""
def generate_player_bubble_segments(row, starting_col, col_width):
    num_segments = 4 # always up to 4 shield bubbles
    col = starting_col
    print "PLAYER_BUBBLES = ["
    for i in range(num_segments):
        print "(" + str(row) + ", " + str(col) + ")"
        if i < num_segments - 1:
            print ",",
        col += col_width
    print "]"

def generate_enemy_bubble_segments(row, starting_col, col_width):
    num_segments = 10
    col = starting_col
    print "ENEMY_BUBBLES = ["
    for i in range(num_segments):
        print "(" + str(row) + ", " + str(col) + ")"
        if i < num_segments - 1:
            print ",",
        col += col_width
    print "]"


#generate_system_segments(1430, 165, 16, 73, 100, 30)
#generate_player_bubble_segments(228, 52, 46)
generate_enemy_hull_segments(255, 876, 22)
generate_enemy_bubble_segments(321, 1668, 36)