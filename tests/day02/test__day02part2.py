import pytest

from advent_of_code_2025.day02.part2 import is_invalid, solve


@pytest.mark.parametrize(
    ("id_", "expected"),
    [
        (12341234, True),
        (123123123, True),
        (1212121212, True),
        (1111111, True),
        (123456, False),
        (1231234, False),
    ],
)
def test__is_invalid(id_: int, *, expected: bool) -> None:
    """Test the is_invalid function for various IDs."""
    result = is_invalid(id_)

    assert result == expected


@pytest.mark.parametrize(
    ("dataset", "expected"),
    [
        ("example_input", 4174379265),
        ("puzzle_input", 17298174201),
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
