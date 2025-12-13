import pytest

from advent_of_code_2025.day03.part1 import find_maximum_joltage, solve


@pytest.mark.parametrize(
    ("bank", "n", "expected"),
    [
        ("987654321111111", 2, 98),
        ("811111111111119", 2, 89),
        ("234234234234278", 2, 78),
        ("818181911112111", 2, 92),
    ],
)
def test__find_maximum_joltage(
    bank: str,
    n: int,
    expected: int,
) -> None:
    """Test finding the maximum joltage for a given bank string."""
    assert find_maximum_joltage(bank, n) == expected


@pytest.mark.parametrize(
    ("dataset", "n", "expected"),
    [
        ("example_input", 2, 357),
        ("puzzle_input", 2, 17031),
    ],
)
def test__solution(
    dataset: str,
    n: int,
    expected: int,
    request: pytest.FixtureRequest,
) -> None:
    """Test the solution for various inputs."""
    data = request.getfixturevalue(dataset)

    result = solve(data, n)

    assert result == expected
