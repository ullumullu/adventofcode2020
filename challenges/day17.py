""" --- Day 17: Conway Cubes ---

Part 1:
Starting with your given initial configuration, simulate six cycles. How many
cubes are left in the active state after the sixth cycle?

Part 2:
Starting with your given initial configuration, simulate six cycles in a
4-dimensional space. How many cubes are left in the active state after
the sixth cycle?
"""

from collections import defaultdict
from functools import cache
from copy import deepcopy
from itertools import product
from typing import Sequence, List, Tuple, Mapping, Any

Cube = Tuple[int, ...]
Cubes = Mapping[Cube, str]

STATE_ACTIVE = "#"
STATE_INACTIVE = "."


def simulate(cubes: Cubes) -> Cubes:
    """Simulate a cycle. Flip all cubes to active that match the ruleset.
    """
    new_cube = defaultdict(lambda: STATE_INACTIVE)
    for cube in cubes:
        neighbours = find_neighbours(cube)
        active_neighbours = sum_active_neighbours(neighbours, cubes)
        if cubes[cube] == STATE_INACTIVE and active_neighbours == 3:
            new_cube[cube] = STATE_ACTIVE
        elif cubes[cube] == STATE_ACTIVE:
            if active_neighbours in (2, 3):
                new_cube[cube] = STATE_ACTIVE
            for neighbour in neighbours:
                if neighbour not in cubes:
                    new_neighbours = find_neighbours(neighbour)
                    k = sum_active_neighbours(new_neighbours, cubes)
                    if k == 3:
                        new_cube[neighbour] = STATE_ACTIVE
    return new_cube


@cache
def find_neighbours(cube: Cube) -> List[Cube]:
    """Find all neighbours for the given cube based on its dimension.

    For instance a three dimensional cube normally has 8 neighbours. A four dimensional
    cube 26.

    Dynamic approach to be usable for any type of n-dimensional cube.
    """
    cube_dimension = len(cube)
    range_dimension = [range(-1, 2)] * cube_dimension
    cubes = []
    for ranges in product(*range_dimension):
        pos_zero = 0
        new_cube = [0] * cube_dimension
        for dimension in range(cube_dimension):
            pos_zero += 1 if ranges[dimension] == 0 else 0
            new_cube[dimension] = cube[dimension] + ranges[dimension]
        if pos_zero != cube_dimension:
            cubes.append(tuple(new_cube))
    return cubes


def sum_active_neighbours(neighbours: Sequence[Cubes], cubes: Cubes) -> int:
    """Amount of neigbours that are active."""
    return sum([1 for pos in neighbours if cubes.get(pos) == STATE_ACTIVE])


def part1(dimension_input: Sequence[str], *, cycles: int) -> int:
    cubes = {(i, j, 0): dimension_input[i][j]
             for i in range(len(dimension_input))
             for j in range(len(dimension_input[0]))}
    for i in range(cycles):
        cubes = simulate(cubes)

    return sum([1 for cube in cubes.values() if cube == STATE_ACTIVE])


def part2(dimension_input: Sequence[str], *, cycles: int) -> int:
    cubes = {(i, j, 0, 0): dimension_input[i][j]
             for i in range(len(dimension_input))
             for j in range(len(dimension_input[0]))}
    for i in range(cycles):
        cubes = simulate(cubes)

    return sum([1 for cube in cubes.values() if cube == STATE_ACTIVE])
