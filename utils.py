"""Utility functions for AoC"""

import functools
import re
import time
from collections.abc import Callable, Iterator, Sequence
from dataclasses import dataclass, field
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


class TimerError(Exception):
    """Exception raised for Timer misuse."""


@dataclass
class Timer:
    """
    A simple timer supporting context manager and decorator usage.

    Args:
        text: Format string for output (receives elapsed time and unit).
        unit: Time unit for display ("s", "ms", "m", "h").
        logger: Callable to output the result (default: print). Set to None to suppress.

    Examples:
        As context manager

        >>> with Timer():  # doctest: +SKIP
        ...     solve()
        Elapsed time: 0.0023 s

        As decorator

        >>> @Timer(unit="ms")  # doctest: +SKIP
        ... def solve():
        ...     pass

        Silent timing (access elapsed time via `t.elapsed`)

        >>> with Timer(logger=None) as t:  # doctest: +SKIP
        ...     result = solve()
        >>> print(f"Took {t.elapsed:.2f}s")  # doctest: +SKIP
    """

    text: str = "Elapsed time: {:0.4f} {:s}"
    unit: str = "ms"
    logger: Callable[[str], None] | None = print
    _start_time: float | None = field(default=None, init=False, repr=False)
    elapsed: float = field(default=0.0, init=False, repr=False)

    _units: dict[str, float] = field(
        default_factory=lambda: {"s": 1, "ms": 1000, "m": 1 / 60, "h": 1 / 3600},
        init=False,
        repr=False,
    )

    def __post_init__(self) -> None:
        if self.unit not in self._units:
            raise TimerError(f'Invalid unit "{self.unit}". Use: s, ms, m, h')

    def start(self) -> None:
        """Start the timer."""
        if self._start_time is not None:
            raise TimerError("Timer already running. Call .stop() first.")
        self._start_time = time.perf_counter()

    def stop(self) -> float:
        """Stop the timer and return elapsed time."""
        if self._start_time is None:
            raise TimerError("Timer not running. Call .start() first.")
        self.elapsed = (time.perf_counter() - self._start_time) * self._units[self.unit]
        self._start_time = None
        if self.logger:
            self.logger(self.text.format(self.elapsed, self.unit))
        return self.elapsed

    def __enter__(self) -> "Timer":
        self.start()
        return self

    def __exit__(self, *exc_info) -> None:
        self.stop()

    def __call__(self, func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with self:
                return func(*args, **kwargs)

        return wrapper
