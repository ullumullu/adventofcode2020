""" --- Day 12: Rain Risk ---

Part 1:
Figure out where the navigation instructions lead. What is the
Manhattan distance between that location and the ship's starting position?
Part 2:
Figure out where the navigation instructions actually lead. What is the
Manhattan distance between that location and the ship's starting position?
"""

from typing import Tuple, List, Dict

# Action N means to move north by the given value
ACTION_N = "N"
# Action S means to move south by the given value
ACTION_S = "S"
# Action E means to move east by the given value
ACTION_E = "E"
# Action W means to move west by the given value
ACTION_W = "W"
# Action L means to turn left the given number of degrees
ACTION_L = "L"
# Action R means to turn right the given number of degrees
ACTION_R = "R"
# Action F means to move forward by the given value in the direction the ship is currently facing.
ACTION_F = "F"


def manhattan_distance(start: Tuple[int, int] = (0, 0),
                       end: Tuple[int, int] = (0, 0)) -> int:
    """More info: https://en.wikipedia.org/wiki/Taxicab_geometry
    """
    return sum([abs(abs(el1)-abs(el2)) for el1, el2 in zip(start, end)])


def parse_instr(instruction: str) -> Tuple[str, int]:
    """Parse the navigation instruction into the operation and its argument."""
    return instruction[:1], int(instruction[1:])


def move(operation: str, argument: int) -> Tuple[int, int]:
    """Calculates the move this operation will do."""
    north, east, south, west = 0, 0, 0, 0
    # Jump to next index
    if operation == ACTION_N:
        north += argument
    elif operation == ACTION_E:
        east += argument
    elif operation == ACTION_S:
        south += argument
    elif operation == ACTION_W:
        west += argument
    return north, east, south, west


def rotate_dir(operation: str, argument: int, curr_dir: int, len_directions: int) -> int:
    """Rotate the direction based on the amount of degrees given."""
    new_dir = curr_dir
    if operation == ACTION_L:
        dir_shift = curr_dir - int(argument / 90)
        new_dir = dir_shift % len_directions
    elif operation == ACTION_R:
        dir_shift = curr_dir + int(argument / 90)
        new_dir = dir_shift % len_directions
    return new_dir


def rotate_wp(operation: str, argument: int, wp: List[int], len_directions: int) -> List[int]:
    """Rotate the waypoints based on the amount of degrees given."""
    rotated_wp = compact(wp)
    if operation == ACTION_L:
        dir_shift = int(argument / 90)
        for _ in range(dir_shift):
            rotated_wp.append(rotated_wp.pop(0))
    elif operation == ACTION_R:
        dir_shift = int(argument / 90)
        for _ in range(dir_shift):
            rotated_wp.insert(0, rotated_wp.pop())
    return rotated_wp


def compact(curr_wp: List[int]) -> List[int]:
    """Calculates the move this operation will do."""
    north, east, south, west = curr_wp
    new_wp = [north, east, south, west]

    dir_ne = 0 if north > south else 2
    dir_zero = 2 if north > south else 0

    new_value = abs(north - south)
    new_wp[dir_ne] = new_value
    new_wp[dir_zero] = 0

    dir_ew = 1 if east > west else 3
    dir_zero = 3 if east > west else 1
    new_value = abs(east - west)
    new_wp[dir_ew] = new_value
    new_wp[dir_zero] = 0

    return new_wp


def execution(wp_north: int = 0, wp_east: int = 0, wp_south: int = 0, wp_west: int = 0):
    """Execution wrapper to execute an operation and returns the index
    of the instruction to execute next.

    It also remembers which instructions were already executed. If the
    instruction was already executed returns -1 to indicate an "infinity loop".
    """
    directions = [ACTION_N, ACTION_E, ACTION_S, ACTION_W]
    context = {
        #  North, East, South, West
        "pos": [0, 0, 0, 0],
        "wp": [wp_north, wp_east, wp_south, wp_west],
        "dir": 1
    }
    with_wp = False
    if sum(context["wp"]) > 0:
        with_wp = True

    def execute_inst(instruction: str) -> Tuple[int, int, int, int]:
        """Execute a single argument"""
        operation, argument = parse_instr(instruction)
        if with_wp:
            context["wp"] = rotate_wp(operation, argument,
                                      context["wp"], len(directions))
            context["wp"] = [curr_wp + move_wp
                             for curr_wp, move_wp in zip(context["wp"], move(operation, argument))]

            if operation == ACTION_F:
                north, east, south, west = context["wp"]
                dir_ne = 0 if north > south else 2
                dir_ew = 1 if east > west else 3
                move_ne = abs(north+south) * argument
                move_ew = abs(east+west) * argument

                context["pos"][dir_ne] += move_ne
                context["pos"][dir_ew] += move_ew

            return context["pos"]

        context["dir"] = rotate_dir(operation, argument,
                                    context["dir"], len(directions))
        if operation == ACTION_F:
            operation = directions[context["dir"]]

        context["pos"] = list(curr_pos + move_pos
                              for curr_pos, move_pos in zip(context["pos"], move(operation, argument)))
        # Return current position
        return context["pos"]

    return execute_inst


def navigate_ship(instructions: List[str]) -> int:
    ship_nav = execution()
    north, east, south, west = 0, 0, 0, 0
    for instruction in instructions:
        north, east, south, west = ship_nav(instruction)

    return manhattan_distance(end=(north-south, east-west))


def navigate_ship_waypoint(instructions: List[str]) -> int:
    ship_nav = execution(wp_north=1, wp_east=10)

    for instruction in instructions:
        north, east, south, west = ship_nav(instruction)

    return manhattan_distance(end=(north-south, east-west))
