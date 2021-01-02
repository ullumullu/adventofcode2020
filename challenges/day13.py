""" --- Day 13: Shuttle Search ---

Part 1:
To save time once you arrive, your goal is to figure out the earliest bus
you can take to the airport. (There will be exactly one such bus.)

Part 2:
What is the earliest timestamp such that all of the listed bus IDs depart
at offsets matching their positions in the list?
"""

import math
from typing import List, Tuple


def part1(earliest_dept: int, bus_lines: List[int]) -> int:
    filtered_bus_lines = [int(bus) for bus in bus_lines if bus != "x"]
    timestamp = earliest_dept
    bus_departing = None
    while not bus_departing:
        for bus_line in filtered_bus_lines:
            departing_now = timestamp % bus_line
            if departing_now == 0:
                bus_departing = bus_line
                return (timestamp - earliest_dept) * bus_departing
        timestamp += 1


def xgcd(a: int, b: int) -> Tuple[int, int, int]:
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)

    Taken from:
    https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
    """
    # pylint: disable=invalid-name
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0


def part2(bus_lines: List[int]) -> int:
    # Calculate the mods for every bus
    bus_mods = {}
    for idx, bus_line in enumerate(bus_lines):
        if bus_line != 'x':
            bus_mods[int(bus_line)] = -idx % int(bus_line)

    # Now we need to iterate through all "moduli" and ignore "x'es"
    filtered_bus_lines = [int(bus) for bus in bus_lines if bus != "x"]

    iterator = None
    iterator_mods = {}
    for bus in filtered_bus_lines:
        if not iterator:
            iterator = bus
            iterator_mods[bus] = bus_mods[bus]
            continue

        # Transform
        val_a = bus
        val_b = iterator
        # Fetching the Bézout coefficients
        _, val_x, val_y = xgcd(val_a, val_b)
        # Using https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Existence_(constructive_proof) # pylint: disable=line-too-long
        proof_solution = val_x * val_a * \
            iterator_mods[val_b] + val_y * val_b * bus_mods[val_a]
        # The product of iterator and bus makes up the proof_solution
        iterator *= bus
        # In this case time is always positive so we need the first positive solution
        # and store it for the next round
        minimal_solution = proof_solution
        if proof_solution > 0:
            minimal_solution = proof_solution + \
                -(int(abs(proof_solution) / iterator) * iterator)

        if proof_solution < 0:
            minimal_solution = proof_solution + \
                (math.ceil(abs(proof_solution) / iterator) * iterator)

        if iterator_mods.get(iterator, None):
            raise Exception()
        iterator_mods[iterator] = minimal_solution

    return abs(iterator_mods[iterator])
