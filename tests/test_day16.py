import os
from pathlib import Path
from typing import List, Tuple
from challenges.day16 import Rules, part1, part2


def _read_input(filename: str) -> Tuple[Rules, List[int], List[List[int]]]:
    """Read the input file."""

    rules = {}
    your_ticket = -1
    nearby_tickets = []
    current_path = Path(os.path.dirname(os.path.realpath(__file__)))
    resource_path = current_path / "resources" / filename

    curr_section = 1
    with resource_path.open("r", encoding="utf-8") as input_file:
        for line in input_file.readlines():
            if line == "\n":
                curr_section += 1
                continue

            if curr_section == 1:
                # First rules
                rule_name, rule_set = line.strip().split(": ")
                rules[rule_name] = []
                for rule in rule_set.split(" or "):
                    rule_from, rule_to = [int(val)
                                          for val in rule.strip().split("-")]
                    rules[rule_name].append((rule_from, rule_to))

            if curr_section == 2:
                # Your Ticket
                ticket = line.strip().split(",")
                if len(ticket) > 1:
                    your_ticket = [int(val) for val in ticket]

            if curr_section == 3:
                # Nearby Tickets
                ticket = line.strip().split(",")
                if len(ticket) > 1:
                    nearby_tickets.append([int(val) for val in ticket])

    return rules, your_ticket, nearby_tickets


def test_sample_input_part1():
    rules, your_ticket, nearby_tickets = _read_input("day16_sample_input.txt")
    assert len(rules) == 3
    assert len(your_ticket) == 3
    assert len(nearby_tickets) == 4
    result = part1(rules, nearby_tickets)
    assert result == 71


def test_puzzle_input_part1():
    rules, your_ticket, nearby_tickets = _read_input("day16_puzzle_input.txt")
    assert len(rules) == 20
    assert len(your_ticket) == 20
    assert len(nearby_tickets) == 237
    result = part1(rules, nearby_tickets)
    print(f"Result: {result}")
    assert result == 25788


def test_sample_input_part2():
    rules, your_ticket, nearby_tickets = _read_input(
        "day16_sample_input_part2.txt")
    assert len(rules) == 3
    assert len(your_ticket) == 3
    assert len(nearby_tickets) == 3
    result = part2(rules, your_ticket, nearby_tickets)
    assert result == 132


def test_puzzle_input_part2():
    rules, your_ticket, nearby_tickets = _read_input(
        "day16_puzzle_input.txt")
    assert len(rules) == 20
    assert len(your_ticket) == 20
    assert len(nearby_tickets) == 237
    result = part2(rules, your_ticket, nearby_tickets)
    print(f"Result: {result}")
    assert result == 3902565915559
