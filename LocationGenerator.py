"""
File to generate location code for some of the locations module
Just so I don't have to retype some of this if it changes
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
Generate list of all enemy hull segments
@:param row of all health segments
@:param col: starting column of first segment
@:param col_width: distance between health segments on the x axis
"""
def generate_enemy_hull_segments(row, starting_col, col_width):
    pass

"""
Generate segment locations for all major systems. Shields, engines, medbay, O2, and weapons

"""
def generate_system_segments(


generate_player_hull_segments(128, 33, 24)