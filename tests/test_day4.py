
import os
from pathlib import Path
from typing import List
import pytest
from challenges.day4 import valid_passports


def _read_input(filename: str) -> List[str]:
    """Read the input file. For now this ignores elements that appear
    more than once and other special cases."""
    passports = []
    current_path = Path(os.path.dirname(os.path.realpath(__file__)))
    image_path = current_path / "resources" / filename
    with image_path.open("r", encoding="utf-8") as input_file:
        ele = {}
        for line in input_file.readlines():
            # New line signal for new passport
            if line == "\n":
                passports.append(ele)
                ele = {}
                continue

            kv_pairs = line.strip().split(" ")
            for kv_pair in kv_pairs:
                key, value = kv_pair.split(":")
                ele[key] = value
        # Always append the last element
        passports.append(ele)
    return passports


def test_sample_input_part1():
    sample_input = _read_input("day4_sample_input.txt")
    assert len(sample_input) == 4
    expected_valid_passwords = 2
    valid = valid_passports(
        sample_input, only_keys=True)
    assert valid == expected_valid_passwords


def test_puzzle_input_part1():
    input_map = _read_input("day4_puzzle_input.txt")
    result = valid_passports(
        input_map, only_keys=True)
    print(f"Result: {result}")
    assert result == 213


@pytest.mark.parametrize("test", [
    {
        "filename": "day4_sample_input_valid.txt",
        "expected_elements": 4,
        "expected_valid": 4
    },
    {
        "filename": "day4_sample_input_invalid.txt",
        "expected_elements": 4,
        "expected_valid": 0
    }
])
def test_sample_input_part2(test):
    sample_input = _read_input(test["filename"])
    assert len(sample_input) == test["expected_elements"]
    valid = valid_passports(sample_input)
    assert valid == test["expected_valid"]


def test_puzzle_input_part2():
    input_map = _read_input("day4_puzzle_input.txt")
    result = valid_passports(input_map)
    print(f"Result: {result}")
    assert result == 147
