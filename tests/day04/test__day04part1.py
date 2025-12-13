import pytest

from advent_of_code_2025.day04.part1 import is_accessible, solve

EXAMPLE_SOLUTION = [
    "..xx.xx@x.",
    "x@@.@.@.@@",
    "@@@@@.x.@@",
    "@.@@@@..@.",
    "x@.@@@@.@x",
    ".@@@@@@@.@",
    ".@.@.@.@@@",
    "x.@@@.@@@@",
    ".@@@@@@@@.",
    "x.x.@@@.x.",
]


@pytest.mark.parametrize(
    ("dataset", "max_adjacent_rolls", "pos", "expected"),
    [
        ("example_input", 4, (x, y), EXAMPLE_SOLUTION[x][y] == "x")
        for x in range(len(EXAMPLE_SOLUTION))
        for y in range(len(EXAMPLE_SOLUTION[0]))
        if EXAMPLE_SOLUTION[x][y] != "."
    ],
)
def test__is_accessible(
    dataset: str,
    max_adjacent_rolls: int,
    pos: tuple[int, int],
    expected: int,
    request: pytest.FixtureRequest,
) -> None:
    """Test if a roll is accessible for a given grid."""
    grid = request.getfixturevalue(dataset)
    x, y = pos
    assert is_accessible(grid, x, y, max_adjacent_rolls) == expected


@pytest.mark.parametrize(
    ("dataset", "max_adjacent_rolls", "expected"),
    [
        ("example_input", 4, 13),
        ("puzzle_input", 4, 1389),
    ],
)
def test__solution(
    dataset: str,
    max_adjacent_rolls: int,
    expected: int,
    request: pytest.FixtureRequest,
) -> None:
    """Test the solution for various inputs."""
    data = request.getfixturevalue(dataset)

    result = solve(data, max_adjacent_rolls)

    assert result == expected
