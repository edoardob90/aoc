#!/usr/bin/env python3
# pylint: disable=invalid-name,too-many-locals,unspecified-encoding
"""AoC day 5, 2023: If You Give A Seed A Fertilizer"""

## Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input"""
    inputs, *blocks = puzzle_input.split("\n\n")
    inputs = [int(x) for x in inputs.split(":")[1].split()]

    return inputs, blocks


def part1(data):
    """Solve part 1"""
    # This was solved with the Wolfram Language


def part2(data):
    """Solve part 2"""
    inputs, blocks = data
    seeds = []
    for i in range(0, len(inputs), 2):
        start, end = inputs[i], inputs[i] + inputs[i + 1]
        seeds.append((start, end))

    for block in blocks:
        ranges = []
        for line in block.splitlines()[1:]:
            ranges.append([int(x) for x in line.split()])

        new_ranges = []
        while seeds:
            start, end = seeds.pop()
            for a, b, c in ranges:
                overlap_start = max(start, b)
                overlap_end = min(end, b + c)

                if overlap_start < overlap_end:
                    new_ranges.append((overlap_start - b + a, overlap_end - b + a))

                    if overlap_start > start:
                        seeds.append((start, overlap_start))
                    if overlap_end < end:
                        seeds.append((overlap_end, end))

                    break
            else:
                new_ranges.append((start, end))

        seeds = new_ranges

    return min(seeds)[0]


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

