import math
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator

OPERATIONS = {
    "+": sum,
    "*": math.prod,
}


class UnknownOperatorError(Exception):
    """Raised when an unknown operator is encountered in a math problem."""

    def __init__(self, operator: str) -> None:
        super().__init__(f"Unknown operator: {operator}")
        self.operator = operator


def transpose(matrix: list[list[str]]) -> list[list[str]]:
    """Transpose a 2D matrix."""
    return [list(row) for row in zip(*matrix, strict=True)]


def parse(data: list[str]) -> Generator[tuple[list[int], str]]:
    """Parse the input data into math problems."""
    problems = transpose([line.strip().split() for line in data if line.strip()])

    for problem in problems:
        *numbers, operator = problem
        yield [int(num) for num in numbers], operator


def solve_problem(numbers: list[int], operator: str) -> int:
    """Solve a single math problem given the numbers and operator."""
    if operator not in OPERATIONS:
        raise UnknownOperatorError(operator)

    return OPERATIONS[operator](int(num) for num in numbers)


def solve(data: list[str]) -> int:
    """Return the sum of all given math problems."""
    return sum(solve_problem(numbers, operator) for numbers, operator in parse(data))
