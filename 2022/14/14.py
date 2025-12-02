# pylint: disable=invalid-name
"""AoC day 14, 2022: Regolith Reservoir"""

# Standard library imports
import pathlib
import sys
from itertools import chain


def partition(l, n, d=None, upto=True):
    """Generate sublists of `l` with length up to `n` and offset `d`"""
    offset = d or n
    return [
        l[i : i + n] for i in range(0, len(l), offset) if upto or len(l[i : i + n]) == n
    ]


def rock_line(x1, y1, x2, y2):
    """Create a line of rock points between (x1, y1) and (x2, y2)"""
    rline = []
    x1, x2, y1, y2 = map(int, (x1, x2, y1, y2))
    delta = max(abs(x1 - x2), abs(y1 - y2))
    for i in range(delta):
        rline.append([x1 + (x2 - x1) * i / delta, y1 + (y2 - y1) * i / delta])
    return rline


def parse(puzzle_input):
    """Parse input"""
    puzzle_input = [list(map(lambda x: x.split(","), line.split(" -> "))) for line in puzzle_input.splitlines()]
    points = [partition(line, 2, 1, upto=False) for line in puzzle_input]

    rock_lines = []
    for p1, p2, in chain.from_iterable(points):
        rock_lines.append(rock_line(*p1, *p2))

    return list(chain.from_iterable(rock_lines))


def part1(data):
    """Solve part 1"""
    return data


def part2(data):
    """Solve part 2"""
    return data


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
