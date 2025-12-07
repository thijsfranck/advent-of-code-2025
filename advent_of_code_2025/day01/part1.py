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

    def apply(self, start: int, positions: int) -> int:
        """Apply the movement to a starting position and return the new position."""
        return (start + self.difference) % positions

    @property
    def difference(self) -> int:
        """Return the signed distance of the movement."""
        match self.direction:
            case "R":
                return self.distance
            case "L":
                return -self.distance
            case _:
                raise UnknownDirectionError(self.direction)


def solve(lines: list[str], starting_position: int, positions: int) -> int:
    """Count how many times the dial lands on position zero."""
    position = starting_position
    solution = 0

    for line in lines:
        movement = Movement.from_string(line)

        position = movement.apply(position, positions)

        if position == 0:
            solution += 1

    return solution
