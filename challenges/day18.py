""" --- Day 18: Operation Order ---

Part 1:
Before you can help with the homework, you need to understand it yourself.
Evaluate the expression on each line of the homework; what is the sum of
the resulting values?

Part 2:
What do you get if you add up the results of evaluating the homework problems
using these new rules?
"""

from typing import List, Sequence, Mapping, Generator


def tokenize(expression_set: str) -> Generator[str, None, None]:
    """Handles input expression and sanitize the output when there are
    parenthesis.

    A expression can consist of parenthes, operators and values.
    e.g. "(9", "8", "+", "6))))" or "((((3".

    Returns:
        A single character to use
    """
    closing_parentheses = []
    for expression in expression_set.split():
        # Handle parentheses
        while expression.startswith("("):
            yield "("
            expression = expression[1:]
        while expression.endswith(")"):
            closing_parentheses.append(")")
            expression = expression[:-1]
        # Yield the "sanitized" expression
        yield expression
        # Return closing parentheses afterwards
        while closing_parentheses:
            yield closing_parentheses.pop()


def transform_posfix(expressions: Sequence[str],
                     operators: Mapping[str, int]) -> Generator[str, None, None]:
    """Transform infix notation to postfix notation.

    Found https://en.wikipedia.org/wiki/Shunting-yard_algorithm so using
    Reverse Polish Notation (RPN).
    """
    operator_stack = []
    for expression in expressions:
        if expression.isdigit():
            yield expression
        elif expression in operators:
            while operator_stack \
                    and operator_stack[-1] in operators \
                    and operators[operator_stack[-1]] >= operators[expression]:
                yield operator_stack.pop()
            operator_stack.append(expression)
        elif expression == "(":
            operator_stack.append(expression)
        elif expression == ")":
            while operator_stack and operator_stack[-1] != "(":
                yield operator_stack.pop()
            # remove ")"
            operator_stack.pop()
        else:
            raise ValueError(f"Unknown expression: {expression}")
    while operator_stack:
        yield operator_stack.pop()


def eval_rpn(tokens) -> int:
    """Takes the postfix expression and returns the result.

    Approach is simple. Add digits to the stack. Once we hit an
    operator we execute the operation with the last two digits added.
    The result gets added to the stack again

    At the end there is one value in the stack which is our result.
    """
    val_stack = []
    for token in tokens:
        if token.isdigit():
            val_stack.append(int(token))
        elif token == "+":
            val_stack.append(val_stack.pop() + val_stack.pop())
        elif token == "*":
            val_stack.append(val_stack.pop() * val_stack.pop())
        else:
            raise ValueError(f"Undefined operator: {token}")
    if len(val_stack) != 1:
        raise Exception(f"Calcuation exception: {val_stack}")
    return val_stack.pop()


def calculate(expression_set: List[str], operators: Mapping[str, int]) -> int:
    return eval_rpn(transform_posfix(tokenize(expression_set), operators))


def part1(caluclations: List[str]) -> int:
    """Calculates the sum of multiple expressions.

    Only supports addition and multiplication. In this part
    both operands have the same precedence.
    """
    operators = {
        "+": 0,
        "*": 0
    }
    return sum(calculate(fnct, operators) for fnct in caluclations)


def part2(caluclations: List[str]) -> int:
    """Calculates the sum of multiple expressions.

    Only supports addition and multiplication. In this part
    addition has precedence over multiplication.
    """
    operators = {
        "+": 1,
        "*": 0
    }
    return sum(calculate(fnct, operators) for fnct in caluclations)
