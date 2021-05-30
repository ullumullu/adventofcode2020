import os
from pathlib import Path
from typing import Tuple, List
from challenges.day19 import part1, part2


def _read_input(filename: str) -> Tuple[List[str], List[str]]:
    """Read the input file."""
    rules = []
    words = []
    current_path = Path(os.path.dirname(os.path.realpath(__file__)))
    resource_path = current_path / "resources" / filename
    read_rules = True
    with resource_path.open("r", encoding="utf-8") as input_file:
        for line in input_file:
            if line == "\n":
                read_rules = False
            elif read_rules:
                rules.append(line.strip())
            else:
                words.append(line.strip())

    return rules, words


def test_sample_input_part1():
    rules, words = _read_input("day19_sample_input.txt")
    assert len(rules) == 6
    assert len(words) == 5
    result = part1(rules, words)
    assert result == 2


def test_puzzle_input_part1():
    rules, words = _read_input("day19_puzzle_input.txt")
    assert len(rules) == 137
    assert len(words) == 308
    result = part1(rules, words)
    print(f"Result: {result}")
    assert result == 115


def test_sample_input_part2():
    rules, words = _read_input("day19_sample_input_2.txt")
    assert len(rules) == 31
    assert len(words) == 15
    result = part2(rules, words)
    assert result == 12


def test_puzzle_input_part2():
    rules, words = _read_input("day19_puzzle_input.txt")
    assert len(rules) == 137
    assert len(words) == 308
    result = part2(rules, words)
    assert result == 237
