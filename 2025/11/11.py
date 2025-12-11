#!/usr/bin/env python3
"""
AoC day 11, 2025: Reactor

Rewritten by me, but 100% inspired by enigma's very elegant solution. Thanks!
https://gist.github.com/enigma/48a04eca829877de13329a45c00b1110
"""

import pathlib
import sys
from collections import defaultdict
from functools import cache, reduce
from itertools import pairwise
from operator import mul


def parse_data(puzzle_input: str):
    """Parse input"""
    graph: defaultdict[str, set[str]] = defaultdict(set)
    for line in puzzle_input.splitlines():
        src, *dest = line.split()
        graph[src[:-1]].update(dest)
    return graph


def paths_factory(graph: defaultdict[str, set[str]]):
    @cache
    def paths(src: str, dst: str) -> int:
        if src == dst:
            return 1
        return sum(paths(d, dst) for d in graph[src])

    return paths


def part1(paths):
    """Solve part 1"""
    return paths("you", "out")


def part2(paths):
    """Solve part 2"""
    waypoints = (
        ("svr", "fft", "dac", "out"),
        ("svr", "dac", "fft", "out"),
    )

    return sum(
        reduce(mul, (paths(src, dst) for src, dst in pairwise(wps)))
        for wps in waypoints
    )


def solve(puzzle_input: str):
    """Solve the puzzle for the given input"""
    data = parse_data(puzzle_input)
    paths = paths_factory(data)
    return part1(paths), part2(paths)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(pathlib.Path(path).read_text().strip())
        print("\n".join(str(s) for s in solutions))
