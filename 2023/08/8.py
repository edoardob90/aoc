#!/usr/bin/env python3
# pylint: disable=invalid-name,too-many-locals,unspecified-encoding
"""AoC day 8, 2023"""

## Standard library imports
import pathlib
import sys
from math import lcm

def parse_data(puzzle_input):
    """Parse input"""
    rules, _, *map_lines = puzzle_input.splitlines()

    maps = {}

    for line in map_lines:
        a, b = line.split(" = ")
        maps[a] = b.strip()[1:-1].split(", ")

    return rules, maps


def part1(data):
    """Solve part 1"""
    rules, maps = data

    current_node = "AAA"
    steps = 0

    while current_node != "ZZZ":
        steps += 1
        current_node = maps[current_node][0 if rules[0] == "L" else 1]
        rules = rules[1:] + rules[0]

    return steps


def part2(data):
    """Solve part 2"""
    rules, maps = data

    starting_from = tuple(k for k in maps.keys() if k.endswith("A"))
    cycles = []

    for current in starting_from:
        steps = 0
        current_rules = rules
        cycle = []
        first_z = None

        while True:
            while steps == 0 or not current.endswith("Z"):
                steps += 1
                current = maps[current][0 if current_rules[0] == "L" else 1]
                current_rules = current_rules[1:] + current_rules[0]

            cycle.append(steps)

            if not first_z:
                first_z = current
                steps = 0
            elif current == first_z:
                break

        cycles.append(cycle)

    return lcm(*[c[0] for c in cycles])


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse_data(puzzle_input)
    # yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
