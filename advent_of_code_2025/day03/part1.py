from collections import deque


class NotEnoughBatteriesError(Exception):
    """Raised when there are not enough batteries to fill the required slots."""

    def __init__(self, bank: str, n: int) -> None:
        self.bank = bank
        self.n = n
        super().__init__(f"Not enough batteries in bank '{bank}' to fill {n} slots.")


def find_maximum_joltage(bank: str, n: int) -> int:
    """Find the maximum joltage for a given bank string and a number of batteries n."""
    if len(bank) < n:
        raise NotEnoughBatteriesError(bank, n)

    stack = deque()
    to_remove = len(bank) - n

    for digit in bank:
        while stack and to_remove > 0 and stack[-1] < digit:
            stack.pop()
            to_remove -= 1

        stack.append(digit)

    return int("".join(stack)[:n])


def solve(data: list[str], n: int) -> int:
    """Find the sum of maximum joltage with n batteries for all banks in the data."""
    return sum(find_maximum_joltage(bank, n) for bank in data)
