""" --- Day 1: Report Repair ---

Part 1:
Find the two entries that sum to 2020; what do you get if you multiply them together?

Part 2:
In your expense report, what is the product of the three entries that sum to 2020?
"""

from math import prod
from typing import List
from itertools import combinations


def find_entries(report: List[int], *, sum_equals: int, elements: int) -> int:
    """This is the first challenge of day1.

    Specifically, they need you to find the two (or three) entries that sum to 2020
    and then multiply those two (or three) numbers together.
    """
    for combination in combinations(report, elements):
        if sum(combination) == sum_equals:
            return prod(combination)
    return -1
