"""
aoc_tools.py -- personal toolset for solving AoC puzzles
"""
import sys
from typing import TypeVar, Generator, Iterable, Tuple, List
from collections import deque, defaultdict, Counter
import itertools

try:
    import regex
except ImportError:
    sys.exit("Please, pip install regex")


def nums(string: List) -> List[int]:
    """Return a list of all numbers found in a string"""
    nums_regex = regex.compile(r"(?P<digits>-?\d+)")
    vals = nums_regex.findall(string)
    return [int(x) for x in vals]
