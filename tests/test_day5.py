import os
from pathlib import Path
from typing import List
import pytest
from challenges.day5 import find_seat


def _read_input() -> List[str]:
    """Read the input file. Every line represents an integer value."""
    input_tickets = []
    current_path = Path(os.path.dirname(os.path.realpath(__file__)))
    image_path = current_path / "resources" / "day5_puzzle_input.txt"
    with image_path.open("r", encoding="utf-8") as input_file:
        for line in input_file:
            input_tickets.append(line.strip())
    return input_tickets


@pytest.mark.parametrize("test", [
    {
        "ticket": "BFFFBBFRRR",
        "expected_row": 70,
        "expected_column": 7,
        "expected_seat_id": 567
    },
    {
        "ticket": "FFFBBBFRRR",
        "expected_row": 14,
        "expected_column": 7,
        "expected_seat_id": 119
    },
    {
        "ticket": "BBFFBBFRLL",
        "expected_row": 102,
        "expected_column": 4,
        "expected_seat_id": 820
    }
])
def test_sample_input_part1(test: dict):
    row, column, seat_id = find_seat(test["ticket"])
    assert row == test["expected_row"]
    assert column == test["expected_column"]
    assert seat_id == test["expected_seat_id"]


def test_puzzle_input_part1():
    input_tickets = _read_input()
    seat_ids = [find_seat(ticket)[2] for ticket in input_tickets]
    highest_id = max(seat_ids)
    print(f"Result: {highest_id}")
    assert highest_id == 919


def test_puzzle_input_part2():
    input_tickets = _read_input()
    seat_ids = sorted([find_seat(ticket)[2] for ticket in input_tickets])
    for ele1, ele2 in zip(seat_ids, seat_ids[1:]):
        # When the diff is two between two elements there is exactly one id missing
        if ele2 - ele1 == 2:
            print(f"Result: {ele1+1}")
            assert ele1+1 == 642
