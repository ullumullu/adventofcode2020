""" --- Day 19: Monster Messages ---

Part 1:
How many messages completely match rule 0?

Part 2:
After updating rules 8 and 11, how many messages completely match rule 0?
"""

from typing import Generator, Sequence, Callable, Dict, Union, Optional

Rule = str
Terminal = str
RuleSet = Union[Terminal, Sequence[Sequence[Rule]]]
StateMachine = Dict[Rule, RuleSet]


def statemachine(rules: Sequence[str]) -> StateMachine:
    """Parses the rules into an (indefinite - part 2) statemachine.

    Returns:
        A statemachine representing all possible states and their transition
    """
    stm = {}
    for line in rules:
        k, rule_exp = line.split(": ")
        # Match terminating state
        # In the context of AoC this matches to "a" or "b"
        if rule_exp.startswith('"'):
            rule = rule_exp[1:-1]
        else:
            rule = []
            sub_rules = rule_exp.split(" | ")
            for sub_rule in sub_rules:
                match_rules = sub_rule.split(" ")
                rule.append(match_rules)
        # Append to statemachine
        stm[k] = rule
    return stm


def check_sub_rule(stm: StateMachine, sub_rule: str, word: str) -> str:
    # We hit an end return the leftover word
    if not sub_rule:
        yield word
    # Sub Rule hasn't been fully evaluated yet
    else:
        index, *sub_rule = sub_rule
        for word in next_state(stm, index, word):
            yield from check_sub_rule(stm, sub_rule, word)


def expand_sub_rules(stm: StateMachine, sub_rules: RuleSet, word: str) -> str:
    """ Expands the set of subrules and checks each of them individually.

    If a rule consist of subrules we need to look at all of them. This
    basically spans up the next possible states from the current position.

    Returns:
        word - that terminated the statemachine
    """
    for sub_rule in sub_rules:
        yield from check_sub_rule(stm, sub_rule, word)


def next_state(stm: StateMachine, index: str, word: str) -> str:
    """Gets the next ruleset and follows all possilbe rules."""
    # NonTerminal
    if isinstance(stm[index], list):
        yield from expand_sub_rules(stm, stm[index], word)
    # Terminal Rule
    elif isinstance(stm[index], str):
        # The first char of the curr word matches to the found terminal
        if word and word[0] == stm[index]:
            yield word[1:]
        # Otherwise the word isn't represented by this statemachine
    else:
        raise Exception("Unexpected state")


def match(stm: StateMachine, word):
    return any(m == '' for m in next_state(stm, '0', word))


def part1(rules: Sequence[str], words: Sequence[str]) -> int:
    stm = statemachine(rules)
    return sum(match(stm, word) for word in words)


def part2(rules: Sequence[str], words: Sequence[str]) -> int:
    stm = statemachine(rules)
    stm['8'] = [['42'], ['42', '8']]
    stm['11'] = [['42', '31'], ['42', '11', '31']]
    return sum(match(stm, word) for word in words)
