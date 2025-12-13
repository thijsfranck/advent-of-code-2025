import pytest

from advent_of_code_2025.day06.part1 import solve, solve_problem


@pytest.mark.parametrize(
    ("numbers", "operator", "expected"),
    [
        ([123, 45, 6], "*", 33210),
        ([328, 64, 98], "+", 490),
        ([51, 387, 215], "*", 4243455),
        ([64, 23, 314], "+", 401),
    ],
)
def test__solve_problem(
    numbers: list[int],
    operator: str,
    expected: int,
) -> None:
    """Test solving individual math problems."""
    result = solve_problem(numbers, operator)

    assert result == expected


@pytest.mark.parametrize(
    ("dataset", "expected"),
    [
        ("example_input", 4277556),
        ("puzzle_input", 4412382293768),
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
