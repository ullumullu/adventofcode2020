""" --- Day 3: Toboggan Trajectory ---

Part 1:
Starting at the top-left corner of your map and following a slope of
right 3 and down 1, how many trees would you encounter?

Part 2:
What do you get if you multiply together the number of trees encountered
on each of the listed slopes?
"""

from typing import List


def frequency_character(flight_map: List[List[str]], *, right: int, down: int, char: str) -> int:
    """ From your starting position at the top-left, check the position
    that is right 3 and down 1. Then, check the position that is right 3
    and down 1 from there, and so on until you go past the bottom of the map.
    """
    hit = 0
    pos_y = 0
    width_map = len(flight_map[0])
    for pos_x in range(down, len(flight_map), down):
        pos_y = (pos_y + right) % width_map
        if flight_map[pos_x][pos_y] == char:
            hit += 1

    return hit
