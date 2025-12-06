"""Utility functions for AoC"""

import re
from collections.abc import Iterator, Sequence
from typing import TypeVar

T = TypeVar("T")


def partition(
    data: Sequence[T],
    n: int,
    d: int | None = None,
    upto: bool = False,
) -> Iterator[Sequence[T]]:
    """
    Generate sublists of `data` with length `n` and offset `d`.

    Comparison with `itertools.pairwise`:
    - `pairwise` creates overlapping pairs with offset=1.
    - `partition` creates chunks of any size with configurable offset `d`.

    Args:
        data: The sequence to partition.
        n: Chunk size (exact unless `upto=True`).
        d: Offset between chunks (default: `n`, i.e., no overlap).
        upto: If True, include trailing partial chunk (like Wolfram's `UpTo`).

    Examples:
        No overlap (default): offset equals chunk size

        >>> list(partition('ABCDEFG', 4))
        ['ABCD']

        Sliding window (offset=1)

        >>> list(partition('ABCDEFG', 4, d=1))
        ['ABCD', 'BCDE', 'CDEF', 'DEFG']

        Include trailing partial chunk

        >>> list(partition('ABCDEFG', 4, upto=True))
        ['ABCD', 'EFG']

        >>> list(partition('ABCDEFG', 4, d=2, upto=True))
        ['ABCD', 'CDEF', 'EFG', 'G']
    """
    offset = d or n
    for i in range(0, len(data), offset):
        chunk = data[i : i + n]
        if upto or len(chunk) == n:
            yield chunk


def ilist(string: str, sep: str | None = None) -> list[int]:
    """
    Parse a structured string into a list of integers.

    Use for predictable, well-formatted input where values are either
    single digits or separated by a known delimiter.

    Comparison with `nums`:
    - `ilist` is for structured input with known format.
    - `nums` extracts integers scattered in arbitrary text.

    Examples:
        >>> ilist("12345")
        [1, 2, 3, 4, 5]

        >>> ilist("1-2-3", sep="-")
        [1, 2, 3]

        >>> ilist("10 20 30", sep=" ")
        [10, 20, 30]
    """
    if sep is None:
        return [int(c) for c in string]
    return [int(x) for x in string.split(sep)]


def nums(string: str) -> list[int]:
    """
    Extract all integers (including negative) from a string.

    Use for messy input where numbers are embedded in text with
    varying delimiters or labels.

    Comparison with `ilist`:
    - `nums` finds all integers anywhere in the string.
    - `ilist` parses structured input with known separators.

    Examples:
        >>> nums("Sensor at x=2, y=18")
        [2, 18]

        >>> nums("target area: x=20..30, y=-10..-5")
        [20, 30, -10, -5]

        >>> nums("mul(44,46)")
        [44, 46]

        >>> nums("no numbers here")
        []
    """
    return [int(x) for x in re.findall(r"-?\d+", string)]
