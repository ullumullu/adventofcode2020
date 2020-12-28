""" --- Day 16: Ticket Translation ---

Part 1:
Consider the validity of the nearby tickets you scanned. What is your ticket
scanning error rate?

Part 2:
Once you work out which field is which, look for the six fields on your ticket
that start with the word departure. What do you get if you multiply those six
values together?
"""

import math
from typing import Tuple, Sequence, Mapping, Set

Ticket = Sequence[int]
Ranges = Sequence[Tuple[int, int]]
Rules = Mapping[str, Ranges]


def rules_apply(value: int, rules: Rules) -> Set[str]:
    result = set()
    for name, ranges in rules.items():
        for rule_from, rule_to in ranges:
            if rule_from <= value <= rule_to:
                result.add(name)
                break
    return result


def part1(rules: Rules, nearby_tickets: Sequence[int]) -> int:
    """Finds all invalid nearby tickets based on the rules defined.

    Adding together all of the invalid values produces
    your ticket scanning error rate
    """
    invalid_values = []
    for ticket in nearby_tickets:
        for value in ticket:
            if not rules_apply(value, rules):
                invalid_values.append(value)
    return sum(invalid_values)


def part2(rules: Rules, your_ticket: Ticket, nearby_tickets: Sequence[Ticket]) -> int:
    """Maps the rules to a specific column.

    Multiply together all of the departure columns.
    """
    mapping = {}
    rows = {}
    for indx, _ in enumerate(your_ticket):
        rows[indx] = set(rules.keys())

    for ticket in nearby_tickets:
        for indx, value in enumerate(ticket):
            res = rules_apply(value, rules)
            if len(res) == 0:
                continue
            rows[indx] = rows[indx].intersection(res)

    while len(mapping) != len(your_ticket):
        for indx, _ in enumerate(rows):
            if len(rows[indx]) == 0:
                continue
            if len(rows[indx]) == 1:
                mapping[indx] = rows[indx].pop()
                continue
            if indx not in mapping:
                rows[indx] = rows[indx].difference(set(mapping.values()))

    return math.prod([your_ticket[key] for key, value in mapping.items() if value.startswith("departure")])
