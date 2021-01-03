import os
from pathlib import Path
from typing import List
import pytest
from challenges.day18 import calculate, part1, part2


def _read_input(filename: str) -> List[str]:
    """Read the input file."""
    calcuations = []
    current_path = Path(os.path.dirname(os.path.realpath(__file__)))
    resource_path = current_path / "resources" / filename
    with resource_path.open("r", encoding="utf-8") as input_file:
        for line in input_file.readlines():
            calcuations.append(line.strip())
    return calcuations


@pytest.mark.parametrize("test", [
    {
        "calc": "1 + (2 * 3) + (4 * (5 + 6))",
        "expected": 51
    },
    {
        "calc": "2 * 3 + (4 * 5)",
        "expected": 26
    },
    {
        "calc": "5 + (8 * 3 + 9 + 3 * 4 * 3)",
        "expected": 437
    },
    {
        "calc": "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))",
        "expected": 12240
    },
    {
        "calc": "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2",
        "expected": 13632
    }
])
def test_single_part1(test):
    operators = {
        "+": 0,
        "*": 0
    }
    result = calculate(test["calc"], operators)
    assert result == test["expected"]


def test_sample_input_part1():
    calculation_input = _read_input("day18_sample_input.txt")
    assert len(calculation_input) == 4
    result = part1(calculation_input)
    assert result == 26335


def test_puzzle_input_part1():
    calculation_input = _read_input("day18_puzzle_input.txt")
    assert len(calculation_input) == 370
    result = part1(calculation_input)
    assert result == 650217205854


@pytest.mark.parametrize("test", [
    {
        "calc": "2 * 3 + (4 * 5)",
        "expected": 46
    },
    {
        "calc": "5 + (8 * 3 + 9 + 3 * 4 * 3)",
        "expected": 1445
    },
    {
        "calc": "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))",
        "expected": 669060
    },
    {
        "calc": "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2",
        "expected": 23340
    }
])
def test_single_part2(test):
    operators = {
        "+": 1,
        "*": 0
    }
    result = calculate(test["calc"], operators)
    assert result == test["expected"]


def test_sample_input_part2():
    calculation_input = _read_input("day18_sample_input.txt")
    assert len(calculation_input) == 4
    result = part2(calculation_input)
    assert result == 693891


def test_puzzle_input_part2():
    calculation_input = _read_input("day18_puzzle_input.txt")
    assert len(calculation_input) == 370
    result = part2(calculation_input)
    assert result == 20394514442037
