from copy import deepcopy
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator


DIRECTIONS = [0, 1, -1]
ROLL_CHAR = "@"


def is_accessible(grid: list[list[str]], x: int, y: int, max_adjacent_rolls: int) -> bool:
    """
    Check if a roll at position (x, y) is accessible by the forklift.

    A forklift can access a roll if there are fewer than `max_adjacent_rolls` adjacent rolls around it.
    The forklift can access rolls from any position around the roll including diagonals.
    """
    bounds_x = range(len(grid))
    bounds_y = range(len(grid[0]))

    adjacent_rolls = 0

    for dx in DIRECTIONS:
        for dy in DIRECTIONS:
            if dx == 0 and dy == 0:
                continue

            nx, ny = x + dx, y + dy

            if nx in bounds_x and ny in bounds_y and grid[nx][ny] == ROLL_CHAR:
                adjacent_rolls += 1

    return adjacent_rolls < max_adjacent_rolls


def _find_accessible_rolls(grid: list[list[str]], max_adjacent_rolls: int) -> Generator[tuple[int, int]]:
    """Find all accessible rolls in the grid."""
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == ROLL_CHAR and is_accessible(grid, x, y, max_adjacent_rolls):
                yield (x, y)


def find_accessible_rolls(grid: list[list[str]], max_adjacent_rolls: int) -> Generator[tuple[int, int]]:
    """Find all accessible rolls in the grid, updating the grid after each batch."""
    working_grid = deepcopy(grid)

    while batch := set(_find_accessible_rolls(working_grid, max_adjacent_rolls)):
        yield from batch
        for roll in batch:
            x, y = roll
            working_grid[x][y] = "."


def solve(grid: list[list[str]], max_adjacent_rolls: int) -> int:
    """Count how many rolls can be accessed by the forklift."""
    return len(set(find_accessible_rolls(grid, max_adjacent_rolls)))
