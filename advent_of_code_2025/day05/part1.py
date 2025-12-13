def is_fresh(id_: int, ranges: list[range]) -> bool:
    """Check if the given id falls within any of the ranges."""
    return any(id_ in r for r in ranges)


def merge(ranges: list[range]) -> list[range]:
    """Merge overlapping ranges."""
    sorted_ranges = sorted(ranges, key=lambda r: r.start)
    merged_ranges = []

    for current in sorted_ranges:
        if not merged_ranges or merged_ranges[-1].stop < current.start:
            merged_ranges.append(current)
        else:
            merged_ranges[-1] = range(
                merged_ranges[-1].start,
                max(merged_ranges[-1].stop, current.stop),
            )

    return merged_ranges


def solve(ranges: list[range], ids: list[int]) -> int:
    """Count the number of ids that fall within any of the ranges."""
    merged_ranges = merge(ranges)
    return sum(is_fresh(id_, merged_ranges) for id_ in ids)
