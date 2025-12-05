"""Utility functions for AoC"""

from collections.abc import Iterator, Sequence
from typing import TypeVar

T = TypeVar("T")


def partition(
    data: Sequence[T],
    n: int,
    d: int | None = None,
    upto: bool = True,
) -> Iterator[Sequence[T]]:
    """
    Generate sublists of `data` with length up to `n` and offset `d`.

    Comparison with `itertools.sliding_window`:
    - `sliding_window` creates overlapping chunks with offset=1 (each window shifts by 1).
    - `partition` creates chunks with configurable offset `d` (default: no overlap).

    Examples:
        >>> list(sliding_window('ABCDEFG', 4))
        [('A','B','C','D'), ('B','C','D','E'), ('C','D','E','F'), ('D','E','F','G')]

        >>> list(partition('ABCDEFG', 4))
        ['ABCD', 'EFG']  # offset=4 (no overlap)

        >>> list(partition('ABCDEFG', 4, d=2))
        ['ABCD', 'CDEF', 'EFG']  # offset=2 (overlaps by 2)

        >>> list(partition('ABCDEFG', 4, d=1))
        ['ABCD', 'BCDE', 'CDEF', 'DEFG']  # offset=1 (equivalent to sliding_window)

        >>> list(partition('ABCDEFG', 4, upto=False))
        ['ABCD']  # only complete chunks
    """
    offset = d or n
    for i in range(0, len(data), offset):
        chunk = data[i : i + n]
        if upto or len(chunk) == n:
            yield chunk


def ilist(string: str, sep: str | None = None) -> list[int]:
    """
    Return a list of integers from a string.

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
