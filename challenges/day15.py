""" --- Day 15: Rambunctious Recitation ---

Part 1:
In this game, the players take turns saying numbers. They begin by taking turns reading
from a list of starting numbers (your puzzle input). Then, each turn consists of considering
the most recently spoken number. Given your starting numbers, what will be the 2020th
number spoken?

Part 2:
Given your starting numbers, what will be the 30000000th number spoken?
"""

from functools import reduce
import operator
from collections import deque, defaultdict
from typing import List


def part1_2(input: List[int], turns: int) -> int:
    last_number = 0
    numbers = {ele: indx+1 for indx, ele in enumerate(input)}
    last_number = input[-1]

    for turn in range(len(input)+1, turns+1):
        last = numbers.get(last_number, 0)
        numbers[last_number] = (turn-1)
        last_number = 0 if last == 0 else (turn-1) - last

    return last_number
