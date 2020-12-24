""" --- Day 8: Handheld Halting ---

Part 1:
Run your copy of the boot code. Immediately before any instruction
is executed a second time, what value is in the accumulator?

Part 2:
Fix the program so that it terminates normally by changing exactly
one jmp (to nop) or nop (to jmp). What is the value of the accumulator
after the program terminates?
"""

from typing import List, Tuple

# Known operations
OPS_NOP = "nop"
OPS_ACC = "acc"
OPS_JMP = "jmp"


def execution(start_index: int = 0):
    """Execution wrapper to execute an operation and returns the index
    of the instruction to execute next.

    It also remembers which instructions were already executed. If the
    instruction was already executed returns -1 to indicate an "infinity loop".
    """
    context = {
        "accumulator": 0,
        "index": start_index,
        "visited": []
    }

    def execute_arg(operation: str, argument: int):
        """Execute a single argument"""
        context["visited"].append(context["index"])
        # Jump to next index
        if operation == OPS_NOP:
            context["index"] += 1
        elif operation == OPS_ACC:
            context["accumulator"] += argument
            context["index"] += 1
        elif operation == OPS_JMP:
            context["index"] += argument
        else:
            raise Exception(f"Unknown operation: {operation}")

        # Infinte Loop Discovered
        if context["index"] in context["visited"]:
            return -1, context["accumulator"]
        # Otherwise return the next execution index
        return context["index"], context["accumulator"]

    return execute_arg


def repair(instructions: List[Tuple[str, int]]) -> Tuple[int, str]:
    """Execute the instruction set and flip every NOP and JMP encountered.

    The "sub execution" is isolated to identify if the flip removes the infinity loop.
    Otherwise continue on the regular exection.
    """
    index = 0
    executor = execution(start_index=index)
    while -1 < index < len(instructions):
        # Pre-execution
        operation, argument = instructions[index]

        flip_cmd = None
        if operation == OPS_NOP:
            flip_cmd = OPS_JMP
        elif operation == OPS_JMP:
            flip_cmd = OPS_NOP

        if flip_cmd:
            dl_executor = execution(start_index=index)
            back_index, _ = dl_executor(flip_cmd, argument)
            while -1 < back_index < len(instructions):
                back_op, back_arg = instructions[back_index]
                back_index, _ = dl_executor(back_op, back_arg)

            if back_index >= len(instructions):
                return index, flip_cmd
        # Couldn't fix the infinity loop yet. Continue regular exection of the program.
        index, _ = executor(operation, argument)

    return None, None


def execute_instructions(instructions: List[Tuple[str, int]], fix_infinity: bool = False) -> int:
    """Executes a simple instruction set of jmp, acc and nop operations.

    Args:
        instructions: instruction set consisting of tuples with (operation, argument)
        fix_infinity: argument to fix an infinty loop before execution

    Returns:
        The sum of all executed acc operations
    """
    if fix_infinity:
        fix_index, fix_operation = repair(instructions)
        _, argument = instructions[fix_index]
        instructions[fix_index] = (fix_operation, argument)

    executor = execution(start_index=0)
    index = 0
    while -1 < index < len(instructions):
        index, value = executor(*instructions[index])
    return value
