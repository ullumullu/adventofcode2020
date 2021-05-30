import os
from pathlib import Path
from typing import List
from challenges.day3 import frequency_character


def _read_input() -> List[str]:
    """Read the input file."""
    travel_map = []
    current_path = Path(os.path.dirname(os.path.realpath(__file__)))
    image_path = current_path / "resources" / "day3_puzzle_input.txt"
    with image_path.open("r", encoding="utf-8") as input_file:
        for line in input_file:
            travel_map.append(str(line.strip()))
    return travel_map


def test_sample_input_part1():
    sample_input = ["..##.......", "#...#...#..", ".#....#..#.", "..#.#...#.#", ".#...##..#.",
                    "..#.##.....", ".#.#.#....#", ".#........#", "#.##...#...", "#...##....#",
                    ".#..#...#.#"]
    expected_trees_hit = 7
    hit_trees = frequency_character(
        sample_input, right=3, down=1, char="#")
    assert hit_trees == expected_trees_hit


def test_puzzle_input_part1():
    input_map = _read_input()
    result = frequency_character(
        input_map, right=3, down=1, char="#")
    print(f"Result: {result}")
    assert result == 276


def test_sample_input_part2():
    sample_input = ["..##.......", "#...#...#..", ".#....#..#.", "..#.#...#.#", ".#...##..#.",
                    "..#.##.....", ".#.#.#....#", ".#........#", "#.##...#...", "#...##....#",
                    ".#..#...#.#"]
    expected_trees_multiplier = 336

    # right, down, expected
    test_paths = [(1, 1, 2), (3, 1, 7), (5, 1, 3), (7, 1, 4), (1, 2, 2)]
    result = 1
    for test_path in test_paths:
        hit_trees = frequency_character(
            sample_input, right=test_path[0], down=test_path[1], char="#")
        assert hit_trees == test_path[2]
        result *= hit_trees

    assert result == expected_trees_multiplier


def test_puzzle_input_part2():
    input_map = _read_input()

    test_paths = [(1, 1, 2), (3, 1, 7), (5, 1, 3), (7, 1, 4), (1, 2, 2)]
    result = 1
    for test_path in test_paths:
        hit_trees = frequency_character(
            input_map, right=test_path[0], down=test_path[1], char="#")
        result *= hit_trees

    print(f"Result: {result}")
    assert result == 7812180000
