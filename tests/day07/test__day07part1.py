import pytest

from advent_of_code_2025.day07.part1 import solve


@pytest.mark.parametrize(
    ("dataset", "expected"),
    [
        ("example_input", 21),
        ("puzzle_input", 1541),
    ],
)
def test__solution(
    dataset: str,
    expected: int,
    request: pytest.FixtureRequest,
) -> None:
    """Test the solution for various inputs."""
    data = request.getfixturevalue(dataset)

    result = solve(data)

    assert result == expected
