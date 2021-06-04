# CodingNomads - Coding Challenge #2: Find the Floor
# Scott Ford
# June 3, 2021

# You are on the ground floor (floor 0) of a tall apartment building. 
# You need to get to a specific floor, but the only directions you have consist of a series of ( and ) characters:

#     Every ( character means to go up one floor.
#     Every ) character means to go down one floor.


def find_floor(directions: str):
    '''iterate through parentheses string to determine current floor'''
    current_floor = 0
    for direction in directions:
        if direction == '(':
            current_floor += 1
        elif direction == ')':
            current_floor -= 1
    return current_floor