from typing import List


def iter_flatten(root):
    """Simple flattener. Does not handle self references during
    the flatterning process.
    """
    if isinstance(root, (list, tuple)):
        for element in root:
            for ele in iter_flatten(element):
                yield ele
    else:
        yield root


def unique_votes_total(groups: List[List[str]]) -> int:
    """Counts the sum of unique answers answered with yes per group.
    """
    votes = 0
    for group in groups:
        votes += len(set(iter_flatten(group)))
    return votes


def unique_votes(groups: List[List[str]]) -> int:
    """Counts the sum of answers intersecting in a group.
    """
    votes = 0
    for group in groups:
        union_group = set(group[0])
        for person in group:
            union_group = union_group.intersection(person)
        votes += len(union_group)
    return votes
