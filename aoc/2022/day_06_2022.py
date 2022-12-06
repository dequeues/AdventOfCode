from typing import Any
from aoc import utils


def get_first_character(group_size: int = 4) -> int:
    for i in range(len(inputdata[0])):
        group_set = set(inputdata[0][i:i+group_size])
        if len(group_set) == group_size:
            return i + group_size

    return 0


@utils.time_func
def part1(*args: Any, **kwargs: Any) -> int:  # pylint: disable=unused-argument
    return get_first_character()


@utils.time_func
def part2(*args: Any, **kwargs: Any) -> int:  # pylint: disable=unused-argument
    return get_first_character(14)


# Fixed test data
inputdata = utils.get_day_data(6, test_data=True)
assert part1(silent=True) == 7  # type: ignore
assert part2(silent=True) == 19  # type: ignore

inputdata = utils.get_day_data(6, test_data=False)
utils.print_result(F'Part 1 answer: {part1()}')
utils.print_result(F'Part 2 answer: {part2()}')
