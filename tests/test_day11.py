import os
from typing import List
from pathlib import Path
from challenges.day11 import calc_used_seats


def _read_input(filename: str) -> List[List[str]]:
    """Read the input file. For now this ignores elements that appear
    more than once and other special cases."""
    seat_plan = []
    current_path = Path(os.path.dirname(os.path.realpath(__file__)))
    image_path = current_path / "resources" / filename
    with image_path.open("r", encoding="utf-8") as input_file:
        for line in input_file.readlines():
            seat_plan.append(list(line.strip()))
    return seat_plan


def test_sample_input_part1():
    seat_plan = _read_input("day11_sample_input.txt")
    assert len(seat_plan) == 10
    assert len(seat_plan[0]) == 10
    result = calc_used_seats(seat_plan)
    assert result == 37


def test_puzzle_input_part1():
    seat_plan = _read_input("day11_puzzle_input.txt")
    assert len(seat_plan) == 91
    assert len(seat_plan[0]) == 97
    result = calc_used_seats(seat_plan)
    print(f"Result: {result}")
    assert result == 2296


def test_sample_input_part2():
    seat_plan = _read_input("day11_sample_input.txt")
    assert len(seat_plan) == 10
    assert len(seat_plan[0]) == 10
    result = calc_used_seats(seat_plan,
                             max_occupied_seats=5,
                             strat="view")
    assert result == 26


def test_puzzle_input_part2():
    seat_plan = _read_input("day11_puzzle_input.txt")
    assert len(seat_plan) == 91
    assert len(seat_plan[0]) == 97
    result = calc_used_seats(seat_plan,
                             max_occupied_seats=5,
                             strat="view")
    print(f"Result: {result}")
    assert result == 2089
