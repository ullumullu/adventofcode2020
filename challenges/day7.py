from typing import Dict, List


def trace(curr_bag: str, bag_rule_set: Dict,
          visited: List[str], baggage_count: int, search_bag_name: str) -> int:
    """Trace route until we find the element with search_bag_name as a depth first search.

    Path is actually a nested List that contains the root element and an array
    with all child paths.
    """
    # For DFS avoid "visiting" bags multiple times
    if search_bag_name and curr_bag in visited:
        return 0
    # Add bag to vistited list
    visited.append(curr_bag)
    # Only relevant for search case to exit early
    if curr_bag == search_bag_name:
        return -1
    # No more sub rules we found a leaf
    if len(bag_rule_set[curr_bag]["rules"]) == 0:
        return 1

    sub_counter = 0
    # Inspect child bags
    for rule in bag_rule_set[curr_bag]["rules"].keys():
        sub_path_count = trace(
            rule, bag_rule_set, visited, baggage_count, search_bag_name)
        # In case of -1 we found the bag we were looking for
        if sub_path_count == -1:
            return -1
        # Add the value of the sub bags
        amount_current_packages = int(bag_rule_set[curr_bag]["rules"][rule])
        sub_counter += amount_current_packages * sub_path_count
        # And the amount of the bags itself if this is not a leaf bag
        if sub_path_count != 1:
            sub_counter += amount_current_packages
    baggage_count += sub_counter
    return baggage_count


def trace_bags_contain(bag_rule_set: Dict, *, name: str) -> int:
    result = 0
    for rule_set_name in bag_rule_set.keys():
        visited = []
        found = trace(rule_set_name, bag_rule_set, visited, 0, name)
        if found == -1 and len(visited) > 1:
            result += 1
    return result


def trace_bags_amount(bag_rule_set: Dict, *, name: str) -> int:
    baggage_count = trace(name, bag_rule_set, [], 0, "")
    return baggage_count
