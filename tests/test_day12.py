import os
from pathlib import Path
from typing import List
from challenges.day12 import manhattan_distance, navigate_ship, navigate_ship_waypoint


def _read_input(filename: str) -> List[List[str]]:
    """Read the input file. For now this ignores elements that appear
    more than once and other special cases."""
    instruction_set = []
    current_path = Path(os.path.dirname(os.path.realpath(__file__)))
    image_path = current_path / "resources" / filename
    with image_path.open("r", encoding="utf-8") as input_file:
        for line in input_file:
            instruction_set.append(str(line.strip()))
    return instruction_set


def test_manhattan_distance():
    dist = manhattan_distance(end=(17, 8))
    assert dist == 25


def test_sample_input_part1():
    instructions = _read_input("day12_sample_input.txt")
    assert len(instructions) == 5
    result = navigate_ship(instructions)
    assert result == 25


def test_puzzle_input_part1():
    instructions = _read_input("day12_puzzle_input.txt")
    assert len(instructions) == 776
    result = navigate_ship(instructions)
    print(f"Result: {result}")
    assert result == 1424


def test_sample_input_part2():
    instructions = _read_input("day12_sample_input.txt")
    assert len(instructions) == 5
    result = navigate_ship_waypoint(instructions)
    assert result == 286


def test_puzzle_input_part2():
    instructions = _read_input("day12_puzzle_input.txt")
    assert len(instructions) == 776
    result = navigate_ship_waypoint(instructions)
    print(f"Result: {result}")
    assert result == 63447
