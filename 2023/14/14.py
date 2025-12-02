#!/usr/bin/env python3
# pylint: disable=invalid-name,too-many-locals,unspecified-encoding
"""AoC day 14, 2023: Parabolic Reflector Dish"""

## Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input"""
    return puzzle_input.splitlines()


def part1(data):
    """Solve part 1"""
    grid = map("".join, list(zip(*data)))
    grid = ("#".join("".join(sorted(list(x), reverse=True)) for x in row.split("#")) for row in grid)
    grid = list(map("".join, list(zip(*grid))))

    return sum(row.count("O") * i for i, row in enumerate(reversed(grid), start=1))


def part2(data):
    """Solve part 2"""
    def cycle(grid):
        for _ in range(4):
            grid = map("".join, zip(*data))
            grid = ("#".join("".join(sorted(tuple(x), reverse=True)) for x in row.split("#")) for row in grid)
            grid = tuple(row[::-1] for row in grid)

        return grid

    grid = tuple(data)
    seen = {grid}
    confs = [grid]
    steps = 0

    while True:
        steps += 1
        grid = cycle(grid)
        if grid in seen:
            break
        seen.add(grid)
        confs.append(grid)

    transient = confs.index(grid)

    print(transient)

    grid = confs[(1_000_000_000 - transient) % (steps - transient) + transient]

    print(grid)

    return sum(row.count("O") * (len(grid) - r) for r, row in enumerate(grid))

    # return sum(row.count("O") * i for i, row in enumerate(reversed(final_grid), start=1))


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
