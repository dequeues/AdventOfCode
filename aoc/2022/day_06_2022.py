from typing import Any
from aoc import utils


@utils.time_func
def part1(*args: Any, **kwargs: Any) -> int:  # pylint: disable=unused-argument
    for i in range(len(inputdata[0])):
        group_set = set(inputdata[0][i:i+4])
        if len(group_set) == 4:
            return i + 4

    return 0


@utils.time_func
def part2(*args: Any, **kwargs: Any) -> int:  # pylint: disable=unused-argument
    return 0


# Fixed test data
inputdata = utils.get_day_data(6, test_data=True)
assert part1(silent=True) == 7  # type: ignore
assert part2(silent=True) == 0  # type: ignore

inputdata = utils.get_day_data(6, test_data=False)
utils.print_result(F'Part 1 answer: {part1()}')
utils.print_result(F'Part 2 answer: {part2()}')
