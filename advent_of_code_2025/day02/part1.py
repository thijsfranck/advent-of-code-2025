from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterator


@dataclass
class Range:
    """Class representing a range of integers."""

    start: int
    end: int

    @classmethod
    def from_string(cls, line: str) -> Range:
        """Create a Range instance from a string like '5-10'."""
        start, end = line.split("-")
        return cls(start=int(start), end=int(end))

    def __iter__(self) -> Iterator[int]:
        """Return an iterator over the range."""
        return iter(range(self.start, self.end + 1))


def is_invalid(id_: int) -> bool:
    """An ID is invalid if it can be divided into two equal halves."""
    as_str = str(id_)

    middle = len(as_str) // 2
    first_half, second_half = as_str[:middle], as_str[middle:]

    return first_half == second_half


def solve(data: str) -> int:
    """Count the sum of all invalid IDs in the given ranges."""
    ranges = [Range.from_string(line) for line in data.split(",")]

    invalid_ids = [id_ for r in ranges for id_ in r if is_invalid(id_)]

    return sum(invalid_ids)
