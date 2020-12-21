from functools import cache
from copy import deepcopy
from typing import List, Tuple, Callable

# Indication of a floor element
FLOOR = "."
# Indication for a seat element occupied by a passenger
SEAT_OCCUPIED = "#"
# Indication for a free seat element
SEAT_FREE = "L"
# Strat for part 1
SEARCH_STRAT_ADJ = "adj"
# Strat for part 2
SEARCH_STRAT_VIEW = "view"
# Generator with a set of all options to calc the neighbours
ADJ_COMBINATIONS = [(x, y) for x in range(-1, 2)
                    for y in range(-1, 2) if (x, y) != (0, 0)]


@cache
def neighbour_positions_adjacent(pos_x: int, pos_y: int,
                                 rows: int, cols: int) -> List[Tuple[int, int]]:
    result = []
    for step_x, step_y in ADJ_COMBINATIONS:
        adj_x = pos_x + step_x
        adj_y = pos_y + step_y
        # Make sure the position is not out of bounds
        if -1 < adj_x < rows and -1 < adj_y < cols:
            result.append((adj_x, adj_y))
    return result


def occupation_adj(seat_plan: List[List[str]], pos_x: int, pos_y: int) -> int:
    rows = len(seat_plan)
    cols = len(seat_plan[pos_x])
    occupied_seats = 0
    for x_adj, y_adj in neighbour_positions_adjacent(pos_x, pos_y, rows, cols):
        if seat_plan[x_adj][y_adj] == SEAT_OCCUPIED:
            occupied_seats += 1
    return occupied_seats


def occupation_view(seat_plan: List[List[str]], x_indx: int, y_indx: int) -> int:
    x_len = len(seat_plan)
    y_len = len(seat_plan[x_indx])
    occupied_seats = 0
    for step_x, step_y in ADJ_COMBINATIONS:
        x_adj = x_indx + step_x
        y_adj = y_indx + step_y
        while True:
            if not(-1 < x_adj < x_len and -1 < y_adj < y_len):
                break
            if seat_plan[x_adj][y_adj] == SEAT_FREE:
                break
            if seat_plan[x_adj][y_adj] == SEAT_OCCUPIED:
                occupied_seats += 1
                break
            x_adj += step_x
            y_adj += step_y

    return occupied_seats


def get_search_strat(strat: str) -> Callable[[List[List[str]], int, int], int]:
    search_strategy = None
    if strat == SEARCH_STRAT_ADJ:
        search_strategy = occupation_adj
    elif strat == SEARCH_STRAT_VIEW:
        search_strategy = occupation_view
    else:
        raise Exception("Only adj and view strategy supported")
    return search_strategy


def calc_used_seats(seat_plan: List[List[str]],
                    max_occupied_seats: int = 4, strat: str = SEARCH_STRAT_ADJ) -> int:
    occupied_seats = 0
    curr_seat_plan = deepcopy(seat_plan)
    new_seat_plan = deepcopy(seat_plan)
    search_strat = get_search_strat(strat)
    while True:
        occupation_changed = False
        for x_indx, _ in enumerate(new_seat_plan):
            for y_indx, _ in enumerate(new_seat_plan[x_indx]):
                curr_seat = curr_seat_plan[x_indx][y_indx]
                # We don't care about "floor"
                if curr_seat == FLOOR:
                    continue
                # Calculate "visible occupied seats"
                adj_occupied = search_strat(curr_seat_plan, x_indx, y_indx)
                # Handle people sitting down or standing up
                if curr_seat == SEAT_FREE and not adj_occupied:
                    new_seat_plan[x_indx][y_indx] = SEAT_OCCUPIED
                    occupied_seats += 1
                    occupation_changed = True
                elif curr_seat == SEAT_OCCUPIED and adj_occupied >= max_occupied_seats:
                    new_seat_plan[x_indx][y_indx] = SEAT_FREE
                    occupied_seats -= 1
                    occupation_changed = True

        if not occupation_changed:
            return occupied_seats

        curr_seat_plan = deepcopy(new_seat_plan)
