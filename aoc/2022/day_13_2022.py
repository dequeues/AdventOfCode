from functools import cmp_to_key
from json import loads
from typing import Any, Union

from aoc import utils


def compare(left: Union[list[int], int], right: Union[list[int], int]) -> int:
    if isinstance(left, int) and isinstance(right, int):
        return left - right
    elif isinstance(left, list) and isinstance(right, list):
        for inner_left, inner_right in zip(left, right):
            inner_res = compare(inner_left, inner_right)
            if inner_res != 0:
                return inner_res
        return compare(len(left), len(right))
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)

    return -999


def decoder_key(packets: list[list[Any]]) -> int:
    packets += [[], [[2]], [[6]]]
    packets.sort(key=cmp_to_key(compare))
    return packets.index([[2]]) * packets.index([[6]])


@ utils.time_func
def part1(*args: Any, **kwargs: Any) -> int:  # pylint: disable=unused-argument
    pairs_in_order: list[int] = []
    for i, pair_string in enumerate(inputdata, 1):
        left, right = list(map(loads, pair_string.split("\n")))
        if compare(left, right) < 0:
            pairs_in_order.append(i)

    return sum(pairs_in_order)


@ utils.time_func
def part2(*args: Any, **kwargs: Any) -> int:  # pylint: disable=unused-argument
    packets: list[Any] = []
    for pair_string in inputdata:
        left, right = map(loads, pair_string.split("\n"))
        packets += [left, right]

    return decoder_key(packets)


day_func_arguments = {"split_delimiter": "\n\n"}

# Fixed test data
inputdata = utils.get_day_data(13, test_data=True, **day_func_arguments)
assert part1(silent=True) == 13  # type: ignore
assert part2(silent=True) == 140  # type: ignore

inputdata = utils.get_day_data(13, test_data=False, **day_func_arguments)
utils.print_result(F'Part 1 answer: {part1()}')
utils.print_result(F'Part 2 answer: {part2()}')
