from pathlib import Path

import pytest


@pytest.fixture
def example_input() -> list[tuple[int, ...]]:
    """Read the example input."""
    example_input_path = Path(__file__).parent / "input/example.txt"

    return [
        tuple(int(value) for value in line.split(",")) for line in example_input_path.read_text().strip().splitlines()
    ]


@pytest.fixture
def puzzle_input() -> list[tuple[int, ...]]:
    """Read the puzzle input."""
    puzzle_input_path = Path(__file__).parent / "input/puzzle.txt"

    return [
        tuple(int(value) for value in line.split(",")) for line in puzzle_input_path.read_text().strip().splitlines()
    ]
