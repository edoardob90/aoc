#!/usr/bin/env python3
# pylint: disable=invalid-name,too-many-locals,unspecified-encoding
"""AoC day 13, 2023: Point of Incidence"""

## Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input"""
    blocks = puzzle_input.split("\n\n")
    return [block.splitlines() for block in blocks]


def part1(data):
    """Solve part 1"""
    def find_mirror(grid):
        for r in range(1, len(grid)):
            above = grid[:r][::-1]
            below = grid[r:]

            to_take = min(len(x) for x in (above, below))

            if above[:to_take] == below[:to_take]:
                return r

        return 0

    total = 0

    for grid in data:
        row = find_mirror(grid)
        total += 100 * row

        col = find_mirror(list(zip(*grid)))
        total += col

    return total


def part2(data):
    """Solve part 2"""
    def find_mirror(grid):
        for r in range(1, len(grid)):
            above = grid[:r][::-1]
            below = grid[r:]

            if sum(sum(0 if a == b else 1 for a, b in zip(x, y)) for x, y in zip(above, below)) == 1:
                return r

        return 0

    total = 0

    for grid in data:
        row = find_mirror(grid)
        total += 100 * row

        col = find_mirror(list(zip(*grid)))
        total += col

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
