import pytest

from advent_of_code_2025.day02.part1 import solve


@pytest.mark.parametrize(
    ("dataset", "expected"),
    [
        ("example_input", 1227775554),
        ("puzzle_input", 12586854255),
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
