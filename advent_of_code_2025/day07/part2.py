from functools import cache

SPLITTER_CHAR = "^"


class StartNotFoundError(Exception):
    """Custom exception raised when the start position is not found in the matrix."""

    def __init__(self) -> None:
        super().__init__("Start position 'S' not found in the matrix.")


def find_start(matrix: list[list[str]]) -> tuple[int, int]:
    """Find the starting position in the matrix."""
    for y, row in enumerate(matrix):
        for x, value in enumerate(row):
            if value == "S":
                return (x, y)

    raise StartNotFoundError


def simulate(matrix: list[list[str]], start: tuple[int, int]) -> int:
    """Return the total number of timelines created by the tachyon beam in the matrix."""
    y_bounds = range(len(matrix))
    x_bounds = range(len(matrix[0]))

    @cache
    def _simulate(pos: tuple[int, int]) -> int:
        x, y = pos

        if not (x in x_bounds and y in y_bounds):
            return 1

        if matrix[y][x] == SPLITTER_CHAR:
            return _simulate((x - 1, y)) + _simulate((x + 1, y))

        return _simulate((x, y + 1))

    return _simulate(start)


def solve(matrix: list[list[str]]) -> int:
    """Solve the problem for the given matrix."""
    start_pos = find_start(matrix)
    return simulate(matrix, start_pos)
