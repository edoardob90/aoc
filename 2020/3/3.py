#!/usr/bin/env python
# pylint: disable=invalid-name,too-many-locals,unspecified-encoding
"""AoC day 3, 2020"""

## Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input"""
    return [
        [1 if pos == "#" else 0 for pos in line] for line in puzzle_input.splitlines()
    ]


def part1(data, right=3, down=1):
    """Solve part 1"""
    start, trees, depth, width = [0, 0], 0, len(data), len(data[0])
    while start[0] < depth:
        trees += data[start[0]][start[1]]
        start = [start[0] + down, (start[1] + right) % width]
    return trees


def part2(data):
    """Solve part 2"""
    total = 1
    for right, down in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
        total *= part1(data, right, down)
    return total


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
