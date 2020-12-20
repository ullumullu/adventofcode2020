from collections import Counter
from typing import List


def jolt_difference(adapters: List[int], start_joltage: int = 0) -> int:
    sorted_adapters = sorted(adapters)
    io_adapters = [start_joltage] + sorted_adapters + [sorted_adapters[-1]+3]
    diff_jolts = [el1 - el2 for el2, el1 in zip(io_adapters, io_adapters[1:])]
    diff_count = Counter(diff_jolts)
    return diff_count[1] * diff_count[3]


def jolt_options(adapters: List[int], start_joltage: int = 0, max_diff: int = 3) -> int:
    sorted_adapters = sorted(adapters)
    final_adapter = int(sorted_adapters[-1])+max_diff
    io_adapters = [start_joltage] + sorted_adapters + [final_adapter]

    option_map = [0] * (final_adapter+1)
    option_map[0] = 1
    for adpt in io_adapters[1:]:
        options_to = [option_map[adpt - back_range]
                      for back_range in range(1, max_diff+1) if adpt >= back_range]
        option_map[adpt] += sum(options_to)

    return option_map[final_adapter]
