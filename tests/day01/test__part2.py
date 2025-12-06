import pytest

from advent_of_code_2025.day01.part2 import solve


@pytest.mark.parametrize(
    ("dataset", "starting_position", "positions", "expected"),
    [
        ("example_input", 50, 100, 6),
        ("puzzle_input", 50, 100, 6223),
    ],
)
def test__solution(
    dataset: str,
    starting_position: int,
    positions: int,
    expected: int,
    request: pytest.FixtureRequest,
) -> None:
    """Test the solution for various inputs."""
    data = request.getfixturevalue(dataset)

    result = solve(data, starting_position, positions)

    assert result == expected
