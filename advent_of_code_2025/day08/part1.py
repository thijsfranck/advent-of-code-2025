import heapq
import math
from collections import defaultdict
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator


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


def build_graph(edgelist: list[Edge], n: int) -> dict[int, set[int]]:
    """
    Build a graph with the n smallest distances from the edgelist.

    The graph is represented as an adjacency list.
    """
    graph = defaultdict(set)

    for edge in heapq.nsmallest(n, edgelist):
        graph[edge.source].add(edge.target)
        graph[edge.target].add(edge.source)

    return graph


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


def solve(data: list[tuple[int, ...]], n: int, m: int) -> int:
    """Calculate the product of the sizes of the m largest cirquits formed by the n smallest distances."""
    edgelist = build_edgelist(data)
    graph = build_graph(edgelist, n)
    return math.prod(sorted([len(circuit) for circuit in find_cirquits(graph)], reverse=True)[:m])
