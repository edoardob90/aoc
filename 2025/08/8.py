#!/usr/bin/env python3
"""AoC day 8, 2025: Playground"""

import pathlib
import sys
from itertools import combinations, islice
from math import prod

from utils import ilist


class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.parents = dict(zip(range(n), range(n)))
        self.sizes = {i: 1 for i in range(n)}

    def find(self, x: int):
        while (y := self.parents[x]) != x:
            x = y
        return x

    def union(self, a: int, b: int) -> bool:
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False

        self.parents[root_b] = root_a
        self.sizes[root_a] += self.sizes[root_b]

        return True

    def root_sizes(self) -> list[int]:
        return [size for box, size in self.sizes.items() if self.parents[box] == box]


def distance(p1: tuple[int, ...], p2: tuple[int, ...]) -> float:
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2


def sort_boxes(boxes: dict[int, tuple[int, ...]]):
    return sorted(
        combinations(boxes.items(), 2),
        key=lambda pair: distance(pair[0][1], pair[1][1]),
    )


def parse_data(puzzle_input: str):
    """Parse input"""

    return {
        i: tuple(ilist(line, ",")) for i, line in enumerate(puzzle_input.splitlines())
    }


def part1(n: int, sorted_pairs, limit: int):
    """Solve part 1"""
    uf = UnionFind(n)
    for (i, _), (j, _) in islice(sorted_pairs, limit):
        uf.union(i, j)

    return prod(
        sorted(
            uf.root_sizes(),
            reverse=True,
        )[:3]
    )


def part2(n: int, sorted_pairs):
    """Solve part 2"""
    uf = UnionFind(n)
    successful = 0
    for (i, x), (j, y) in sorted_pairs:
        if uf.union(i, j):
            successful += 1
            if successful == uf.n - 1:
                return x[0] * y[0]


def solve(puzzle_input: str, example: bool = False):
    """Solve the puzzle for the given input"""
    data = parse_data(puzzle_input)
    sorted_pairs = sort_boxes(data)
    limit = 10 if example else 1000  # Part 1 max number of pairs to connect
    return part1(len(data), sorted_pairs, limit), part2(len(data), sorted_pairs)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(
            pathlib.Path(path).read_text().strip(),
            example="example" in path,
        )
        print("\n".join(str(s) for s in solutions))
