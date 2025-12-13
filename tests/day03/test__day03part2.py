import pytest

from advent_of_code_2025.day03.part2 import find_maximum_joltage, solve


@pytest.mark.parametrize(
    ("bank", "n", "expected"),
    [
        ("987654321111111", 12, 987654321111),
        ("811111111111119", 12, 811111111119),
        ("234234234234278", 12, 434234234278),
        ("818181911112111", 12, 888911112111),
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
        ("example_input", 12, 3121910778619),
        ("puzzle_input", 12, 168575096286051),
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
