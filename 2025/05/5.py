#!/usr/bin/env python3
"""AoC day 5, 2025: Cafeteria"""

import pathlib
import sys
from bisect import bisect_left
from itertools import starmap

from utils import ilist


def parse_data(puzzle_input: str):
    """Parse input"""

    def interval_union(*intervals: list[int]) -> list[list[int]]:
        union = []
        (x, y), *rest = sorted(intervals, key=lambda t: t[0])
        for a, b in rest:
            if y >= a:
                y = max(y, b)
            else:
                union.append([x, y])
                x, y = a, b
        union.append([x, y])
        return union

    ids, ingredients = puzzle_input.split("\n\n")
    ids = [ilist(line, "-") for line in ids.split("\n")]
    ingredients = [int(num) for num in ingredients.split("\n")]
    return interval_union(*ids), ingredients


def part1(data):
    """Solve part 1"""

    def is_member_linear(element: int, *intervals: list[int]) -> bool:
        # Linear search is O(n)
        return any(interval[0] <= element <= interval[1] for interval in intervals)

    def is_member_log(element: int, *intervals: list[int]) -> bool:
        # Binary search is O(log n)
        where = max(0, bisect_left(intervals, element, key=lambda x: x[0]) - 1)
        return intervals[where][0] <= element <= intervals[where][1]

    return sum(is_member_log(i, *data[0]) for i in data[1])


def part2(data):
    """Solve part 2"""
    return sum(starmap(lambda x, y: y - x + 1, data[0]))


def solve(puzzle_input: str):
    """Solve the puzzle for the given input"""
    data = parse_data(puzzle_input)
    return part1(data), part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(pathlib.Path(path).read_text().strip())
        print("\n".join(str(s) for s in solutions))
