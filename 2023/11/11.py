#!/usr/bin/env python3
# pylint: disable=invalid-name,too-many-locals,unspecified-encoding
"""AoC day 11, 2023: Cosmic Expansion"""

## Standard library imports
import pathlib
import sys


def dist_sum(positions: list[int], expansion: int = 2) -> int:
    total = 0
    open_dist = 0
    current = positions[0]
    count = 1

    for n in positions[1:]:
        if n > current:
            dist_to_prev = (n - current - 1) * expansion + 1
            open_dist += count * dist_to_prev
        total += open_dist
        count += 1
        current = n

    return total


def parse_data(puzzle_input):
    """Parse input"""
    x_pos = []
    y_pos = []

    for y, line in enumerate(puzzle_input.splitlines()):
        for x, char in enumerate(line):
            if char == "#":
                x_pos.append(x)
                y_pos.append(y)

    x_pos.sort()
    y_pos.sort()

    return x_pos, y_pos


def part1(data):
    """Solve part 1"""
    x_pos, y_pos = data
    return dist_sum(x_pos) + dist_sum(y_pos)


def part2(data):
    """Solve part 2"""
    x_pos, y_pos = data
    return dist_sum(x_pos, 1_000_000) + dist_sum(y_pos, 1_000_000)


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
