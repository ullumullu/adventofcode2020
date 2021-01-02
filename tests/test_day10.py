import os
from typing import List
from pathlib import Path
from challenges.day10 import jolt_difference, jolt_options


def _read_input(filename: str) -> List[int]:
    """Read the input file.
    """
    joltage_data = []
    current_path = Path(os.path.dirname(os.path.realpath(__file__)))
    image_path = current_path / "resources" / filename
    with image_path.open("r", encoding="utf-8") as input_file:
        for line in input_file.readlines():
            joltage_data.append(int(line.strip()))
    return joltage_data


def test_sample_input_small_part1():
    joltage_data = _read_input("day10_sample_input_small.txt")
    assert len(joltage_data) == 11
    result = jolt_difference(joltage_data)
    assert result == 35


def test_sample_input_large_part1():
    joltage_data = _read_input("day10_sample_input_large.txt")
    assert len(joltage_data) == 31
    result = jolt_difference(joltage_data)
    assert result == 220


def test_puzzle_input_part1():
    joltage_data = _read_input("day10_puzzle_input.txt")
    assert len(joltage_data) == 92
    result = jolt_difference(joltage_data)
    print(f"Result: {result}")
    assert result == 1820


def test_sample_input_small_part2():
    joltage_data = _read_input("day10_sample_input_small.txt")
    assert len(joltage_data) == 11
    result = jolt_options(joltage_data)
    assert result == 8


def test_sample_input_large_part2():
    joltage_data = _read_input("day10_sample_input_large.txt")
    assert len(joltage_data) == 31
    result = jolt_options(joltage_data)
    assert result == 19208


def test_puzzle_input_part2():
    joltage_data = _read_input("day10_puzzle_input.txt")
    assert len(joltage_data) == 92
    result = jolt_options(joltage_data)
    print(f"Result: {result}")
    assert result == 3454189699072
