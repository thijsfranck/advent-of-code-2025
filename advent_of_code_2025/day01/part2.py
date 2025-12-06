from dataclasses import dataclass


class UnknownDirectionError(Exception):
    """Exception raised for unknown movement directions."""

    def __init__(self, direction: str) -> None:
        super().__init__(f"Unknown direction: {direction}")
        self.direction = direction


@dataclass
class Movement:
    """Class representing a movement instruction."""

    direction: str
    distance: int

    @classmethod
    def from_string(cls, line: str) -> Movement:
        """Create a Movement instance from a string like 'R2' or 'L5'."""
        direction, distance = line[0], line[1:]  # The first character is the direction, the rest is the distance
        return cls(direction=direction, distance=int(distance))

    def apply(self, start: int, positions: int) -> tuple[int, int]:
        """
        Apply the movement to a starting position.

        Return the number of times position zero is crossed and the new position.
        """
        if self.direction == "R":
            zero_passes, end = divmod(start + self.distance, positions)

        elif self.direction == "L":
            zero_passes, end = divmod(start - self.distance, positions)

            if start == 0:
                zero_passes += 1

            if end == 0:
                zero_passes -= 1

        else:
            raise UnknownDirectionError(self.direction)

        return abs(zero_passes), end


def solve(lines: list[str], starting_position: int, positions: int) -> int:
    """Count how many times the dial lands on position zero."""
    position = starting_position
    solution = 0

    for line in lines:
        movement = Movement.from_string(line)

        zero_crossings, position = movement.apply(position, positions)
        solution += zero_crossings

    return solution
