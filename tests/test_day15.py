import pytest

from challenges.day15 import part1_2


@pytest.mark.parametrize("test", [
    {
        "input": [0, 3, 6],
        "expected": 436,
        "turns": 2020
    },
    {
        "input": [1, 3, 2],
        "expected": 1,
        "turns": 2020
    },
    {
        "input": [2, 1, 3],
        "expected": 10,
        "turns": 2020
    },
    {
        "input": [1, 2, 3],
        "expected": 27,
        "turns": 2020
    },
    {
        "input": [2, 3, 1],
        "expected": 78,
        "turns": 2020
    },
    {
        "input": [3, 2, 1],
        "expected": 438,
        "turns": 2020
    },
    {
        "input": [3, 1, 2],
        "expected": 1836,
        "turns": 2020
    },
])
def test_sample_input_part1(test):
    result = part1_2(test["input"], test["turns"])
    assert result == test["expected"]


def test_puzzle_input_part1():
    result = part1_2([9, 19, 1, 6, 0, 5, 4], 2020)
    assert result == 1522


def test_puzzle_input_part2():
    result = part1_2([9, 19, 1, 6, 0, 5, 4], 30000000)
    assert result == 18234
