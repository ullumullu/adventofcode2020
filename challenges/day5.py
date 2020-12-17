from typing import Tuple, Iterator


def binary_range_search(search_cmds: Iterator[str],
                        search_range: Tuple[int, int]) -> Tuple[int, int]:
    """

    In this case partition contains the indication which part of the range to keep.
    L --> keep left half of the range
    R --> keep right half of the range

    """
    for search_cmd in search_cmds:
        diff = int((search_range[1] - search_range[0]) / 2)
        if search_cmd == "L":
            search_range = (search_range[0], search_range[0]+diff)
        elif search_cmd == "R":
            search_range = (search_range[1]-diff, search_range[1])
    return search_range


def find_seat(bord_pass: str, total_rows: int = 128, total_cols: int = 8) -> Tuple[int, int, int]:
    """Parses the airlines binary space partitioning to return the row and column.

    The first 7 characters will either be F or B; these specify exactly one of the
    128 rows on the plane (numbered 0 through 127). Each letter tells you which half
    of a region the given seat is in.

    The last three characters will be either L or R; these specify exactly one of
    the 8 columns of seats on the plane (numbered 0 through 7).
    """
    # Row
    row_range = (0, total_rows-1)
    row_search = map(lambda cmd: "L" if cmd ==
                     "F" else "R", list(bord_pass[:7]))
    row = binary_range_search(row_search, row_range)
    # Col
    col_range = (0, total_cols-1)
    col_search = list(bord_pass[7:])
    col = binary_range_search(col_search, col_range)
    # Id
    seat_id = row[0] * 8 + col[0]
    return (row[0], col[0], seat_id)
