
import os
from pathlib import Path
from typing import List
from challenges.day6 import unique_votes_total, unique_votes


def _read_input(filename: str) -> List[str]:
    """Read the input file. For now this ignores elements that appear
    more than once and other special cases."""
    group_answers = []
    current_path = Path(os.path.dirname(os.path.realpath(__file__)))
    image_path = current_path / "resources" / filename
    with image_path.open("r", encoding="utf-8") as input_file:
        group = []
        for line in input_file:
            # New line signal for new passport
            if line == "\n":
                group_answers.append(group)
                group = []
                continue
            group.append(list(line.strip()))
        # Always append the last element
        group_answers.append(group)
    return group_answers


def test_sample_input_part1():
    sample_input = _read_input("day6_sample_input.txt")
    assert len(sample_input) == 5
    votes = unique_votes_total(sample_input)
    assert votes == 11


def test_puzzle_input_part1():
    group_voting = _read_input("day6_puzzle_input.txt")
    votes = unique_votes_total(group_voting)
    print(f"Result: {votes}")
    assert votes == 6683


def test_sample_input_part2():
    sample_input = _read_input("day6_sample_input.txt")
    assert len(sample_input) == 5
    votes = unique_votes(sample_input)
    assert votes == 6


def test_puzzle_input_part2():
    group_voting = _read_input("day6_puzzle_input.txt")
    votes = unique_votes(group_voting)
    print(f"Result: {votes}")
    assert votes == 3122
