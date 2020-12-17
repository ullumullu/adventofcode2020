import os
from pathlib import Path
from typing import List
from challenges.day2 import validate_passwords_frequency, validate_passwords_position


def _read_input() -> List[str]:
    """Read the input file. Every line represents an integer value."""
    password_list = []
    current_path = Path(os.path.dirname(os.path.realpath(__file__)))
    image_path = current_path / "resources" / "day2_puzzle_input.txt"
    with image_path.open("r", encoding="utf-8") as input_file:
        for line in input_file.readlines():
            password_list.append(str(line.strip()))
    return password_list


def test_sample_input_part1():
    sample_input = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
    expected_valid = 2
    valid_passwords = validate_passwords_frequency(sample_input)
    assert valid_passwords == expected_valid


def test_puzzle_input_part1():
    input_passwords = _read_input()
    result = validate_passwords_frequency(input_passwords)
    print(f"Result: {result}")
    assert result == 603


def test_sample_input_part2():
    sample_input = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
    expected_valid = 1
    valid_passwords = validate_passwords_position(sample_input)
    assert valid_passwords == expected_valid


def test_puzzle_input_part2():
    input_passwords = _read_input()
    result = validate_passwords_position(input_passwords)
    print(f"Result: {result}")
    assert result == 404
