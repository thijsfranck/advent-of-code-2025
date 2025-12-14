import heapq
import math
from collections import defaultdict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator


def distance(source: tuple[int, ...], target: tuple[int, ...]) -> float:
    """Calculate the Euclidean distance between two points."""
    return math.sqrt(sum(pow(abs(s - t), 2) for s, t in zip(source, target, strict=True)))


def build_edgelist(data: list[tuple[int, ...]]) -> list[tuple[float, tuple[int, int]]]:
    """Build an edgelist for the given data points ordered by distance."""
    size = len(data)
    result = []

    for i in range(size):
        for j in range(i + 1, size):
            heapq.heappush(result, (distance(data[i], data[j]), (i, j)))

    return result


def build_graph(edgelist: list[tuple[float, tuple[int, int]]], n: int) -> dict[int, dict[int, float]]:
    """
    Build a graph with the n smallest distances from the edgelist.

    The graph is represented as an adjacency list.
    """
    graph: dict[int, dict[int, float]] = defaultdict(lambda: defaultdict(float))

    for distance, edge in heapq.nsmallest(n, edgelist):
        source, target = edge
        graph[source][target] = distance
        graph[target][source] = distance

    return graph


def find_cirquit(graph: dict[int, dict[int, float]], node: int, visited: set[int], cirquit: set[int]) -> set[int]:
    """
    Find the cirquit to which the given node belongs using depth-first search.

    A cirquit is defined as all nodes reachable from the starting node.
    """
    visited.add(node)

    for neighbor, weight in graph[node].items():
        if weight > 0 and neighbor not in visited:
            cirquit = find_cirquit(graph, neighbor, visited, {*cirquit, neighbor})

    return cirquit


def find_cirquits(graph: dict[int, dict[int, float]]) -> Generator[set[int]]:
    """Find all cirquits in the given graph."""
    visited = set()

    for node in graph:
        if node not in visited and len(cirquit := find_cirquit(graph, node, visited, {node})) > 1:
            yield cirquit


def solve(data: list[tuple[int, ...]], n: int, m: int) -> int:
    """Calculate the product of the sizes of the m largest cirquits formed by the n smallest distances."""
    edgelist = build_edgelist(data)
    graph = build_graph(edgelist, n)
    return math.prod(sorted([len(circuit) for circuit in find_cirquits(graph)], reverse=True)[:m])
