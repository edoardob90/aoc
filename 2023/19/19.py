#!/usr/bin/env python3
# pylint: disable=invalid-name,too-many-locals,unspecified-encoding
"""AoC day 19, 2023: Aplenty"""

## Standard library imports
import pathlib
import sys
from operator import gt, lt


OPS = {
    "<": lt,
    ">": gt,
}


def parse_data(puzzle_input):
    """Parse input"""
    wf, rt = puzzle_input.split("\n\n")
    workflows = {}
    for line in wf.splitlines():
        name, rules = line[:-1].split("{")
        *cmps, fallback = rules.split(",")
        workflows[name] = [[], fallback]
        for cmp in cmps:
            rule, dest = cmp.split(":")
            opr, op, val = rule[0], rule[1], int(rule[2:])
            workflows[name][0].append((opr, op, val, dest))

    ratings = []
    for line in rt.splitlines():
        item = {}
        for rating in line[1:-1].split(","):
            k, v = rating.split("=")
            item[k] = int(v)
        ratings.append(item)

    return workflows, ratings



# @Timer(name="Part 1", text="{name}: {milliseconds:.1f} ms")
def part1(data):
    """Solve part 1"""

    def accept(item, key="in"):
        if key == "R":
            return False
        if key == "A":
            return True

        rules, fallback = workflows[key]
        for opr, op, val, dest in rules:
            if OPS[op](item[opr], val):
                return accept(item, dest)

        return accept(item, fallback)

    total = 0
    workflows, ratings = data
    for r in ratings:
        if accept(r):
            total += sum(r.values())

    return total


# @Timer(name="Part 2", text="{name}: {milliseconds:.1f} ms")
def part2(data):
    """Solve part 2"""

    def count(ranges, key="in"):
        if key == "R":
            return 0
        if key == "A":
            prod = 1
            for lo, hi in ranges.values():
                prod *= hi - lo + 1
            return prod

        rules, fallback = workflows[key]

        total = 0

        for opr, op, val, dest in rules:
            lo, hi = ranges[opr]
            if op == "<":
                true = (lo, min(val - 1, hi))
                false = (max(val, lo), hi)
            else:
                true = (max(val + 1, lo), hi)
                false = (lo, min(val, hi))

            if true[0] <= true[1]:
                copy = dict(ranges)
                copy[opr] = true
                total += count(copy, dest)

            if false[0] <= false[1]:
                ranges[opr] = false
            else:
                break
        else:
            total += count(ranges, fallback)

        return total


    workflows, _ = data

    return count({letter: (1, 4000) for letter in "xmas"})



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
