import heapq
import math
from collections import defaultdict
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator


class NoCompleteCirquitError(Exception):
    """Custom exception raised when no complete cirquit is found in the graph."""

    def __init__(self) -> None:
        super().__init__("No complete cirquit found in the graph.")


@dataclass
class Edge:
    """Class representing an edge in the graph."""

    distance: float
    source: int
    target: int

    def __lt__(self, other: Edge) -> bool:
        return self.distance < other.distance


def distance(source: tuple[int, ...], target: tuple[int, ...]) -> float:
    """Calculate the Euclidean distance between two points."""
    return math.sqrt(sum(pow(abs(s - t), 2) for s, t in zip(source, target, strict=True)))


def build_edgelist(data: list[tuple[int, ...]]) -> list[Edge]:
    """Build an edgelist for the given data points ordered by distance."""
    size = len(data)
    result = []

    for i in range(size):
        for j in range(i + 1, size):
            heapq.heappush(result, Edge(distance=distance(data[i], data[j]), source=i, target=j))

    return result


def find_cirquit(graph: dict[int, set[int]], node: int, visited: set[int], cirquit: set[int]) -> set[int]:
    """
    Find the cirquit to which the given node belongs using depth-first search.

    A cirquit is defined as all nodes reachable from the starting node.
    """
    visited.add(node)

    neighbors = graph[node]
    cirquit.update(neighbors)

    for neighbor in neighbors:
        if neighbor not in visited:
            cirquit = find_cirquit(graph, neighbor, visited, cirquit)

    return cirquit


def find_cirquits(graph: dict[int, set[int]]) -> Generator[set[int]]:
    """Find all cirquits in the given graph."""
    visited = set()

    for node in graph:
        if node not in visited:
            yield find_cirquit(graph, node, visited, {node})


def solve(data: list[tuple[int, ...]]) -> int:
    """Calculate the product of the x-coordinates of the final two points that form the complete cirquit."""
    graph = defaultdict(set)
    cirquit = set()

    edgelist = build_edgelist(data)

    while edge := heapq.heappop(edgelist):
        if edge.source in cirquit and edge.target in cirquit:  # The cirquit does not expand
            continue

        graph[edge.source].add(edge.target)
        graph[edge.target].add(edge.source)

        cirquit = next(find_cirquits(graph), set())

        if len(cirquit) != len(data):  # The first cirquit is not complete yet
            continue

        source_x, *_ = data[edge.source]
        target_x, *_ = data[edge.target]

        return source_x * target_x

    raise NoCompleteCirquitError
