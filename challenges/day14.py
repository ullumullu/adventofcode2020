""" --- Day 14: Docking Data ---

Part 1:
Execute the initialization program. What is the sum of all values left in
memory after it completes? (Do not truncate the sum to 36 bits.)

Part 2:
Execute the initialization program using an emulator for a version 2 decoder
chip. What is the sum of all values left in memory after it completes?
"""

from typing import Callable, List, Tuple

# Indicator in the instruction set that this instruction is a new mask
INDICATOR_MASK = -1


def part1(instructions: List[Tuple[int, str]]) -> int:
    """Find the sum of all values in memory after running all commands.

    Applies the mask in two steps. Reason is that this mask basically
    overwrites the input values to whatever is defined in the mask.

    Hence all bits set to 1 in the mask will overwrite the result to 1.

    The first mask is and-ed with the value to set all mask values to 0 in the result.
    The second mask is or-ed with the value to set all mask values to 1 in the result.
    """
    memory = {}
    for pos, value in instructions:
        if pos == INDICATOR_MASK:
            # Set value to 0
            mask_and = int("1"*36, 2)  # 0xFFFFFFFFF
            # Set value to 1
            mask_or = 0
            for indx, bit in enumerate(value):
                if bit == "0":
                    mask_and ^= 1 << (35 - indx)
                if bit == "1":
                    mask_or ^= 1 << (35 - indx)
            continue
        memory[pos] = (int(value) & mask_and) | mask_or

    return sum(memory.values())


def part2(instructions: List[Tuple[int, str]]) -> int:
    """Find the sum of all values in memory after running all commands.

    Applies the mask in two steps. In this part the position is masked with
    floating bits so these have to be pre-adjusted to 0. Afterwards a list
    of adress masks is applied.
    """
    memory = {}
    for pos, value in instructions:
        # Create new masks
        if pos == INDICATOR_MASK:
            masks_or = [0]
            # Set the floating bits in the value to 0 to manipulate
            # the result with all or masks
            floating_mask = int("1"*36, 2)
            for indx, bit in enumerate(value):
                if bit == "1":
                    for mask_pos, mask in enumerate(masks_or):
                        mask ^= 1 << (35 - indx)
                        masks_or[mask_pos] = mask
                if bit == "X":
                    floating_mask ^= 1 << (35 - indx)
                    masks_copy = masks_or.copy()  # Not optimal: 36-bit 'X' requires 288GB
                    for mask in masks_copy:
                        mask ^= 1 << (35 - indx)
                        masks_or.append(mask)
            continue
        # Calculate all positions
        for mask in masks_or:
            new_pos = (pos & floating_mask) | mask
            memory[new_pos] = int(value)

    return sum(memory.values())
