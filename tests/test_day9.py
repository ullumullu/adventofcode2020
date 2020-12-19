import os
from typing import List
from pathlib import Path
from challenges.day9 import find_invalid_xmas_value, find_contigous_set


def _read_input(filename: str) -> List[int]:
    """Read the input file. For now this ignores elements that appear
    more than once and other special cases."""
    xmas_data = []
    current_path = Path(os.path.dirname(os.path.realpath(__file__)))
    image_path = current_path / "resources" / filename
    with image_path.open("r", encoding="utf-8") as input_file:
        for line in input_file.readlines():
            xmas_data.append(int(line.strip()))
    return xmas_data


def test_sample_input_part1():
    sample_xmas_data = _read_input("day9_sample_input.txt")
    assert len(sample_xmas_data) == 20
    invalid_data = find_invalid_xmas_value(sample_xmas_data, preamble=5)
    assert invalid_data == 127


def test_puzzle_input_part1():
    puzzle_xmas_data = _read_input("day9_puzzle_input.txt")
    assert len(puzzle_xmas_data) == 1000
    invalid_data = find_invalid_xmas_value(puzzle_xmas_data, preamble=25)
    print(f"Result: {invalid_data}")
    assert invalid_data == 57195069


def test_sample_input_part2():
    sample_xmas_data = _read_input("day9_sample_input.txt")
    assert len(sample_xmas_data) == 20
    cracked_code = find_contigous_set(sample_xmas_data, 127)
    assert cracked_code == 62


def test_puzzle_input_part2():
    puzzle_xmas_data = _read_input("day9_puzzle_input.txt")
    assert len(puzzle_xmas_data) == 1000
    cracked_code = find_contigous_set(puzzle_xmas_data, 57195069)
    print(f"Result: {cracked_code}")
    assert cracked_code == 7409241
