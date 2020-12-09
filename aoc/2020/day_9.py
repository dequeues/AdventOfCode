from itertools import permutations
from typing import Union
import common  # noqa pylint: disable=unused-import
import utils


inputdata = list(map(int, utils.get_day_data(9)))
PREAMBLE = 25


def get_invalid() -> int:
    for i in range(PREAMBLE, len(inputdata)):
        solutions = [
            a + b for (a, b) in permutations(inputdata[i - PREAMBLE:i], 2)
        ]
        if inputdata[i] not in solutions:
            return int(inputdata[i])

    return 0


def find_contiguous(start: int, check: int) -> Union[list[int], bool]:  # noqa pylint: disable=unsubscriptable-object
    total = 0
    for i in range(start, len(inputdata)):
        total += inputdata[i]
        if total == check:
            return inputdata[start:(i+1)]
        elif total > check:
            return False
    return False


def part1() -> int:
    return get_invalid()


def part2(found: int) -> int:
    for i in range(0, len(inputdata)):
        is_contiguous: Union[list[int], bool] = find_contiguous(i, found)  # noqa pylint: disable=unsubscriptable-object
        if isinstance(is_contiguous, list):
            return min(is_contiguous) + max(is_contiguous)

    return 0


p1: int = part1()
print(F'Part 1 answer: {p1}')
print(F'Part 2 answer: {part2(p1)}')
