import os
from pathlib import Path
from typing import List, Tuple
from challenges.day14 import part1, part2, INDICATOR_MASK


def _read_input(filename: str) -> List[Tuple[int, str]]:
    """Read the input file.
    """
    instructions = []
    current_path = Path(os.path.dirname(os.path.realpath(__file__)))
    image_path = current_path / "resources" / filename
    with image_path.open("r", encoding="utf-8") as input_file:
        for line in input_file:
            position, value = line.strip().split(" = ")
            if position == "mask":
                position = INDICATOR_MASK
            else:
                position = int(position.strip("mem[").strip("]"))
            instructions.append((position, value))
    return instructions


def test_sample_input_part1():
    instructions = _read_input("day14_sample_input.txt")
    assert len(instructions) == 4
    result = part1(instructions)
    assert result == 165


def test_puzzle_input_part1():
    instructions = _read_input("day14_puzzle_input.txt")
    assert len(instructions) == 545
    result = part1(instructions)
    assert result == 9967721333886


def test_sample_input_part2():
    instructions = _read_input("day14_sample_input_2.txt")
    assert len(instructions) == 4
    result = part2(instructions)
    assert result == 208


def test_puzzle_input_part2():
    instructions = _read_input("day14_puzzle_input.txt")
    assert len(instructions) == 545
    result = part2(instructions)
    assert result == 4355897790573
