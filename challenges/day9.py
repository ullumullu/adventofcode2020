from collections import deque
from typing import List


def in_preamble(preamble, value):
    for indx, first_preamble in enumerate(preamble):
        second_preamble = value - first_preamble
        try:
            if preamble.index(second_preamble) != indx:
                return True
        except ValueError:
            continue
    return False


def find_invalid_xmas_value(xmas_data: List[int], preamble: int) -> int:
    for indx in range(preamble, len(xmas_data)):
        cur_preamble = xmas_data[indx-preamble:indx]
        val = xmas_data[indx]
        if not in_preamble(cur_preamble, val):
            return val
    return -1


def find_contigous_set(xmas_data: List[int], sum_value: int) -> int:
    curr_set = deque([])
    for data in xmas_data:
        curr_set.append(data)
        while curr_set and sum(curr_set) > sum_value:
            curr_set.popleft()
        if sum(curr_set) == sum_value:
            return min(curr_set) + max(curr_set)
    return -1
