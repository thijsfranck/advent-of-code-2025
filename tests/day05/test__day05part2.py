import pytest

from advent_of_code_2025.day05.part2 import solve


@pytest.mark.parametrize(
    ("dataset", "expected"),
    [
        ("example_input", 14),
        ("puzzle_input", 355555479253787),
    ],
)
def test__solution(
    dataset: str,
    expected: int,
    request: pytest.FixtureRequest,
) -> None:
    """Test the solution for various inputs."""
    ranges, _ = request.getfixturevalue(dataset)

    result = solve(ranges)

    assert result == expected
