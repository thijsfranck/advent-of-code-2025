import pytest

from advent_of_code_2025.day05.part1 import solve


@pytest.mark.parametrize(
    ("dataset", "expected"),
    [
        ("example_input", 3),
        ("puzzle_input", 756),
    ],
)
def test__solution(
    dataset: str,
    expected: int,
    request: pytest.FixtureRequest,
) -> None:
    """Test the solution for various inputs."""
    ranges, ids = request.getfixturevalue(dataset)

    result = solve(ranges, ids)

    assert result == expected
