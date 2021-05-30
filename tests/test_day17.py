import os
from pathlib import Path
from typing import List
from challenges.day17 import part1, part2


def _read_input(filename: str) -> List[str]:
    """Read the input file."""
    dimension_input = []
    current_path = Path(os.path.dirname(os.path.realpath(__file__)))
    resource_path = current_path / "resources" / filename
    with resource_path.open("r", encoding="utf-8") as input_file:
        for line in input_file:
            dimension_input.append(line.strip())
    return dimension_input


def test_sample_input_part1():
    dimension_input = _read_input("day17_sample_input.txt")
    assert len(dimension_input) == 3
    assert len(dimension_input[0]) == 3
    result = part1(dimension_input, cycles=6)
    assert result == 112


def test_puzzle_input_part1():
    dimension_input = _read_input("day17_puzzle_input.txt")
    assert len(dimension_input) == 8
    assert len(dimension_input[0]) == 8
    result = part1(dimension_input, cycles=6)
    print(f"Result: {result}")
    assert result == 295


def test_sample_input_part2():
    dimension_input = _read_input("day17_sample_input.txt")
    assert len(dimension_input) == 3
    assert len(dimension_input[0]) == 3
    result = part2(dimension_input, cycles=6)
    assert result == 848


def test_puzzle_input_part2():
    dimension_input = _read_input("day17_puzzle_input.txt")
    assert len(dimension_input) == 8
    assert len(dimension_input[0]) == 8
    result = part2(dimension_input, cycles=6)
    print(f"Result: {result}")
    assert result == 1972
