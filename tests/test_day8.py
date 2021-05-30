import os
from pathlib import Path
from typing import List, Tuple
from challenges.day8 import execute_instructions


def _read_input(filename: str) -> List[Tuple[str, int]]:
    """Read the input file.
    """
    instructions = []
    current_path = Path(os.path.dirname(os.path.realpath(__file__)))
    image_path = current_path / "resources" / filename
    with image_path.open("r", encoding="utf-8") as input_file:
        for line in input_file:
            operation, argument = line.strip().split(" ")
            instructions.append((operation, int(argument)))
    return instructions


def test_sample_input_part1():
    sample_instructions = _read_input("day8_sample_input.txt")
    assert len(sample_instructions) == 9
    count = execute_instructions(sample_instructions)
    assert count == 5


def test_puzzle_input_part1():
    puzzle_instructions = _read_input("day8_puzzle_input.txt")
    assert len(puzzle_instructions) == 612
    count = execute_instructions(puzzle_instructions)
    print(f"Result: {count}")
    assert count == 1810


def test_sample_input_part2():
    sample_instructions = _read_input("day8_sample_input.txt")
    assert len(sample_instructions) == 9
    count = execute_instructions(sample_instructions, fix_infinity=True)
    assert count == 8


def test_puzzle_input_part2():
    puzzle_instructions = _read_input("day8_puzzle_input.txt")
    assert len(puzzle_instructions) == 612
    count = execute_instructions(puzzle_instructions, fix_infinity=True)
    print(f"Result: {count}")
    assert count == 969
