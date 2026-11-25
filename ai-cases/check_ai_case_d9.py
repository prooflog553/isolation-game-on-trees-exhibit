"""Exact replay of two marked-forest positions from the diameter-nine exploration."""
from functools import lru_cache


def position(block_counts):
    """For each component, join a marked hub to the midpoint of each P7."""
    next_vertex = len(block_counts)
    edges = []
    for hub, count in enumerate(block_counts):
        for _ in range(count):
            first = next_vertex
            next_vertex += 7
            edges.extend((v, v + 1) for v in range(first, first + 6))
            edges.append((hub, first + 3))
    return next_vertex, edges, (1 << len(block_counts)) - 1


def solve(n, edges, initially_marked):
    neighborhoods = [1 << vertex for vertex in range(n)]
    pairs = []
    for a, b in edges:
        u, v = 1 << a, 1 << b
        neighborhoods[a] |= v
        neighborhoods[b] |= u
        pairs.append(u | v)

    @lru_cache(maxsize=None)
    def moves(covered, staller):
        # An edge survives exactly when neither endpoint is covered.
        targets = 0
        for endpoints in pairs:
            if not covered & endpoints:
                targets |= endpoints
        if not targets:
            return 0
        successor_values = (
            moves(covered | neighborhood, not staller)
            for neighborhood in neighborhoods
            if neighborhood & targets
        )
        return 1 + (max if staller else min)(successor_values)

    answer = (moves(initially_marked, False), moves(initially_marked, True))
    moves.cache_clear()
    return answer


def main():
    for counts, expected in (((1, 2), (9, 10)), ((2, 2), (13, 13))):
        n, edges, marked = position(counts)
        values = solve(n, edges, marked)
        if values != expected:
            raise SystemExit(f"Unexpected values on {n} vertices: {values}")
        print(f"{n} vertices: D-start {values[0]}, S-start {values[1]}")


if __name__ == "__main__":
    main()
