from pathlib import Path

import pytest


@pytest.fixture
def example_input() -> list[str]:
    """Read the example input."""
    example_input_path = Path(__file__).parent / "input/example.txt"

    return example_input_path.read_text().splitlines()


@pytest.fixture
def puzzle_input() -> list[str]:
    """Read the puzzle input."""
    puzzle_input_path = Path(__file__).parent / "input/puzzle.txt"

    return puzzle_input_path.read_text().splitlines()
