import os
from pathlib import Path
from typing import List, Tuple
from challenges.day13 import part1, part2


def _read_input(filename: str) -> Tuple[int, List[int]]:
    """Read the input file. For now this ignores elements that appear
    more than once and other special cases."""
    bus_lines = []
    current_path = Path(os.path.dirname(os.path.realpath(__file__)))
    image_path = current_path / "resources" / filename
    with image_path.open("r", encoding="utf-8") as input_file:
        earliest_departure = int(input_file.readline().strip())
        bus_lines = [bus.strip()
                     for bus in input_file.readline().strip().split(",")]

    return earliest_departure, bus_lines


def test_sample_input_part1():
    earliest_departure, bus_lines = _read_input("day13_sample_input.txt")
    assert len(bus_lines) == 8
    result = part1(earliest_departure, bus_lines)
    assert result == 295


def test_puzzle_input_part1():
    earliest_departure, bus_lines = _read_input("day13_puzzle_input.txt")
    assert earliest_departure == 1007153
    assert len(bus_lines) == 102
    result = part1(earliest_departure, bus_lines)
    print(f"Result: {result}")
    assert result == 2165


def test_sample_input_part2():
    _, bus_lines = _read_input("day13_sample_input.txt")
    assert len(bus_lines) == 8
    result = part2(bus_lines)
    assert result == 1068781


def test_sample_input_part2_small():
    _, bus_lines = _read_input("day13_sample_input_small.txt")
    assert len(bus_lines) == 4
    result = part2(bus_lines)
    assert result == 3417


def test_sample_input_part2_custom():
    _, bus_lines = _read_input("day13_sample_input_custom.txt")
    # assert len(bus_lines) == 5
    result = part2(bus_lines)
    assert result == 39


def test_puzzle_input_part2():
    _, bus_lines = _read_input("day13_puzzle_input.txt")
    assert len(bus_lines) == 102
    result = part2(bus_lines)
    print(f"Result: {result}")
    assert result == 534035653563227
