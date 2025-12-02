#!/usr/bin/env python3
# pylint: disable=invalid-name,too-many-locals,unspecified-encoding
"""AoC day 23, 2023: A Long Walk"""

## Standard library imports
import pathlib
import sys


def parse_data(puzzle_input, p2=False):
    """Parse input"""
    grid = puzzle_input.splitlines()

    start = (0, grid[0].index("."))
    end = (len(grid) - 1, grid[-1].index("."))

    points = [start, end]

    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char == "#":
                continue

            neighs = 0

            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < len(grid) and 0 <= nc < len(row) and grid[nr][nc] != "#":
                    neighs += 1

            if neighs >= 3:
                points.append((r, c))

    graph = {pt: {} for pt in points}

    if p2:
        STEPS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        DIRS = {s: STEPS for s in "^>v<."}
    else:
        DIRS = {
            "^": [(-1, 0)],
            ">": [(0, 1)],
            "v": [(1, 0)],
            "<": [(0, -1)],
            ".": [(-1, 0), (0, 1), (1, 0), (0, -1)], # order: up, right, down, left
        }

    for sr, sc in points:
        stack = [(0, sr, sc)]
        seen = {(sr, sc)}

        while stack:
            n, r, c = stack.pop()

            if n != 0 and (r, c) in points:
                graph[(sr, sc)][(r, c)] = n
                continue

            for dr, dc in DIRS[grid[r][c]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[nr]) and grid[nr][nc] != "#":
                    if (nr, nc) not in seen:
                        stack.append((n + 1, nr, nc))
                        seen.add((nr, nc))

    print(graph)

    return start, end, graph


def solve_part(data):
    """Solve part 1 & 2"""
    start, end, graph = data
    seen = set()

    def longest_path(node):
        if node == end:
            return 0

        max_length = -float("inf")

        seen.add(node)

        for next_node, steps in graph[node].items():
            if next_node not in seen:
                max_length = max(max_length, steps + longest_path(next_node))

        seen.remove(node)

        return max_length

    return longest_path(start)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    yield solve_part(parse_data(puzzle_input))
    # yield solve_part(parse_data(puzzle_input, p2=True))


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
