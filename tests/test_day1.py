import os
from pathlib import Path
from typing import List
from challenges.day1 import find_entries


def _read_input() -> List[int]:
    """Read the input file. Every line represents an integer value."""
    input_report_repair = []
    current_path = Path(os.path.dirname(os.path.realpath(__file__)))
    image_path = current_path / "resources" / "day1_puzzle_input.txt"
    with image_path.open("r", encoding="utf-8") as input_file:
        for line in input_file.readlines():
            input_report_repair.append(int(line.strip()))
    return input_report_repair


def test_sample_input_part1():
    sample_input = [1721, 979, 366, 299, 675, 1456]
    expected = 514579
    result = find_entries(sample_input, sum_equals=2020, elements=2)
    assert result == expected


def test_puzzle_input_part1():
    input_report_repair = _read_input()
    result = find_entries(input_report_repair, sum_equals=2020, elements=2)
    print(f"Result: {result}")
    assert result == 935419


def test_sample_input_part2():
    sample_input = [1721, 979, 366, 299, 675, 1456]
    expected = 241861950
    result = find_entries(sample_input, sum_equals=2020, elements=3)
    assert result == expected


def test_puzzle_input_part2():
    input_report_repair = _read_input()
    result = find_entries(input_report_repair, sum_equals=2020, elements=3)
    print(f"Result: {result}")
    assert result == 49880012
