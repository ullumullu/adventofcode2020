from typing import List


def frequency_character(map: List[List[str]], *, right: int, down: int, char: str) -> int:
    """ From your starting position at the top-left, check the position
    that is right 3 and down 1. Then, check the position that is right 3
    and down 1 from there, and so on until you go past the bottom of the map.
    """
    hit = 0
    x = 0
    y = 0
    width_map = len(map[0])
    for x in range(down, len(map), down):
        y = (y + right) % width_map
        if map[x][y] == char:
            hit += 1

    return hit
