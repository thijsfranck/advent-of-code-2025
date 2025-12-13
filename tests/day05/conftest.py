from pathlib import Path

import pytest


def parse_input(text: str) -> tuple[list[range], list[int]]:
    """Parse the input into ranges and ids."""
    ranges, ids = text.strip().split("\n\n")
    return (
        [range(int(lower), int(upper) + 1) for lower, upper in (line.split("-") for line in ranges.splitlines())],
        [int(id_) for id_ in ids.splitlines()],
    )


@pytest.fixture
def example_input() -> tuple[list[range], list[int]]:
    """Read the example input."""
    example_input_path = Path(__file__).parent / "input/example.txt"

    return parse_input(example_input_path.read_text())


@pytest.fixture
def puzzle_input() -> tuple[list[range], list[int]]:
    """Read the puzzle input."""
    puzzle_input_path = Path(__file__).parent / "input/puzzle.txt"

    return parse_input(puzzle_input_path.read_text())
