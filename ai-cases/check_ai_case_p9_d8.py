# SPDX-License-Identifier: MIT
"""Replay the P9 opening failure and the two diameter-eight example trees.

Written for this research exhibit on 2026-11-21; this is a new exact replay,
not an original historical search script or a proof for arbitrary trees.
Uses only the Python standard library. Run from the repository root:

    python3 -I ai-cases/check_ai_case_p9_d8.py

Add --stats to print cache sizes and elapsed times. All reported game values
count the entire game, including a prescribed first move when one is given.
"""

import argparse
from collections import deque
from functools import lru_cache
from time import perf_counter


def tree_diameter(n, edges):
    """Validate a finite simple tree and return its diameter in edges."""
    if n < 1 or len(edges) != n - 1:
        raise ValueError("A tree must have n >= 1 vertices and n - 1 edges")
    neighbors = [[] for _ in range(n)]
    seen = set()
    for u, v in edges:
        if not (0 <= u < n and 0 <= v < n) or u == v:
            raise ValueError("Invalid tree edge")
        edge = tuple(sorted((u, v)))
        if edge in seen:
            raise ValueError("Repeated tree edge")
        seen.add(edge)
        neighbors[u].append(v)
        neighbors[v].append(u)
    diameter = 0
    for start in range(n):
        distances = [-1] * n
        distances[start] = 0
        queue = deque([start])
        while queue:
            u = queue.popleft()
            for v in neighbors[u]:
                if distances[v] == -1:
                    distances[v] = distances[u] + 1
                    queue.append(v)
        if -1 in distances:
            raise ValueError("The graph is disconnected")
        diameter = max(diameter, max(distances))
    return diameter


def diameter_eight_tree(with_leaf):
    """Center 0 joins midpoints 4, 11, 18 of paths 1..7, 8..14, 15..21.

    In the second example, vertex 22 is an additional leaf adjacent to 0.
    """
    edges = []
    for first in (1, 8, 15):
        edges.extend((v, v + 1) for v in range(first, first + 6))
        edges.append((0, first + 3))
    if with_leaf:
        edges.append((0, 22))
    return 23 if with_leaf else 22, edges


def solve_openings(n, edges):
    """Return the free D-start value and the value of every D first move.

    A state records covered vertices and whose turn it is. An edge survives
    iff neither endpoint is covered. A vertex is legal iff its closed
    neighborhood meets an endpoint of such an edge. In particular, a vertex
    already covered may still be legal. Every legal move strictly increases
    the covered set, so the recursion is finite.
    """
    neighborhoods = [1 << vertex for vertex in range(n)]
    pairs = []
    for u, v in edges:
        neighborhoods[u] |= 1 << v
        neighborhoods[v] |= 1 << u
        pairs.append((1 << u) | (1 << v))

    @lru_cache(maxsize=None)
    def remaining(covered, staller):
        targets = 0
        for endpoints in pairs:
            if not covered & endpoints:
                targets |= endpoints
        if targets == 0:
            return 0
        # Equal successor states have equal values; keep each state once.
        successors = {
            covered | neighborhood
            for neighborhood in neighborhoods
            if neighborhood & targets
        }
        values = (remaining(state, not staller) for state in successors)
        return 1 + (max(values) if staller else min(values))

    free_value = remaining(0, False)
    # Every vertex is a legal first move in these nontrivial connected trees.
    first_values = [1 + remaining(neighborhood, True)
                    for neighborhood in neighborhoods]
    if free_value != min(first_values):
        raise RuntimeError("The free value differs from the best first move")
    cache_info = remaining.cache_info()
    remaining.cache_clear()
    return free_value, first_values, cache_info


def require_equal(label, actual, expected):
    if actual != expected:
        raise SystemExit(f"FAIL: {label}: expected {expected}, got {actual}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stats", action="store_true",
                        help="show memoized state counts and elapsed times")
    args = parser.parse_args()

    started = perf_counter()
    edges = [(v, v + 1) for v in range(8)]
    require_equal("P9 diameter", tree_diameter(9, edges), 8)
    free, openings, cache = solve_openings(9, edges)
    require_equal("P9 first-move values", openings,
                  [4, 3, 3, 4, 4, 4, 3, 3, 4])
    require_equal("P9 free D-start", free, 3)
    print("P9 first moves (vertices 1..9):", " ".join(map(str, openings)))
    print(f"P9: free D-start {free}; center-first {openings[4]}")
    if args.stats:
        print(f"  P9 cache: {cache.currsize} states; "
              f"{perf_counter() - started:.3f} seconds")

    for with_leaf, expected_free in ((False, 9), (True, 10)):
        started = perf_counter()
        n, edges = diameter_eight_tree(with_leaf)
        diameter = tree_diameter(n, edges)
        require_equal(f"{n}-vertex diameter", diameter, 8)
        free, openings, cache = solve_openings(n, edges)
        require_equal(f"{n}-vertex free D-start", free, expected_free)
        require_equal(f"{n}-vertex center-first", openings[0], 10)
        print(f"D8, {n} vertices: diameter {diameter}; "
              f"free D-start {free}; center-first {openings[0]}")
        if args.stats:
            print(f"  D8 cache: {cache.currsize} states; "
                  f"{perf_counter() - started:.3f} seconds")

    print("23 vertices: floor(3n/7) = 9; ceil(3n/7) = 10")
    print("PASS: all three finite examples match the stated values.")


if __name__ == "__main__":
    main()
