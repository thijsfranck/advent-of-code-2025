import pytest

from advent_of_code_2025.day08.part1 import solve


@pytest.mark.parametrize(
    ("dataset", "n", "m", "expected"),
    [
        ("example_input", 10, 3, 40),
        ("puzzle_input", 1000, 3, 117000),
    ],
)
def test__solution(
    dataset: str,
    n: int,
    m: int,
    expected: int,
    request: pytest.FixtureRequest,
) -> None:
    """Test the solution for various inputs."""
    data = request.getfixturevalue(dataset)

    result = solve(data, n, m)

    assert result == expected
