#!/usr/bin/env python
# pylint: disable=invalid-name,too-many-locals,unspecified-encoding
"""AoC day 4, 2019"""

## Standard library imports
import pathlib
import sys
from collections import Counter


def parse_data(puzzle_input):
    """Parse input"""
    start, end = [int(x) for x in puzzle_input.split("-")]
    return range(start, end + 1)


def part1(data):
    """Solve part 1"""
    count = 0
    for pwd in data:
        pwd = list(str(pwd))
        if pwd == sorted(pwd) and len(pwd) != len(set(pwd)):
            count += 1
    return count


def part2(data):
    """Solve part 2"""
    count = 0
    for pwd in data:
        pwd = list(str(pwd))
        if pwd == sorted(pwd):
            c = Counter(pwd).values()
            if list(c).count(2) >= 1:
                count += 1
    return count


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(path)
        print("\n".join(str(solution) for solution in solutions))
