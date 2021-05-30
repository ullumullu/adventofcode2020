
import os
from pathlib import Path
from typing import List
from challenges.day7 import trace_bags_contain, trace_bags_amount


def _read_input(filename: str) -> List[str]:
    """Read the input file. For now this ignores elements that appear
    more than once and other special cases."""
    bag_rule_set = {}
    current_path = Path(os.path.dirname(os.path.realpath(__file__)))
    image_path = current_path / "resources" / filename
    with image_path.open("r", encoding="utf-8") as input_file:
        for line in input_file:

            name_bag, contains_bags = map(
                lambda bag: bag.strip(), line.strip(". \n").split("contain"))

            bag_rule_set[name_bag] = {
                "rules": {}
            }

            bag_rules = [tuple(bag_rule.split(" ", 1))
                         for bag_rule in contains_bags.split(", ")
                         if "no other bags" not in bag_rule]

            for bag_rule in bag_rules:
                amount = bag_rule[0]
                name = bag_rule[1] if int(
                    amount) > 1 else bag_rule[1] + ("s")

                bag_rule_set[name_bag]["rules"][name] = amount
    return bag_rule_set


def test_sample_input_part1():
    sample_input = _read_input("day7_sample_input.txt")
    root_bags = trace_bags_contain(sample_input, name="shiny gold bags")
    assert root_bags == 4


def test_puzzle_input_part1():
    puzzle_input = _read_input("day7_puzzle_input.txt")
    root_bags = trace_bags_contain(puzzle_input, name="shiny gold bags")
    print(f"Result: {root_bags}")
    assert root_bags == 197


def test_sample_input_part2():
    sample_input = _read_input("day7_sample_input.txt")
    amount_bags = trace_bags_amount(sample_input, name="shiny gold bags")
    assert amount_bags == 32


def test_sample_input_part2_2():
    sample_input = _read_input("day7_sample_input_2.txt")
    amount_bags = trace_bags_amount(sample_input, name="shiny gold bags")
    assert amount_bags == 126


def test_puzzle_input_part2():
    puzzle_input = _read_input("day7_puzzle_input.txt")
    amount_bags = trace_bags_amount(puzzle_input, name="shiny gold bags")
    print(f"Result: {amount_bags}")
    assert amount_bags == 85324
