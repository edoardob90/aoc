#!/usr/bin/env python
# pylint: disable=invalid-name,too-many-locals,unspecified-encoding
"""AoC day 6, 2020: Custom Customs"""

## Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input"""
    return puzzle_input.split("\n\n")


def part1(data):
    """Solve part 1"""
    answers = 0
    for group in data:
        answers += len(set(group.replace("\n", "")))
    return answers


def part2(data):
    """Solve part 2"""


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
