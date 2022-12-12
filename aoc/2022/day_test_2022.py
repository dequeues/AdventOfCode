from typing import Any

from aoc import utils


@utils.time_func
def part1(*args: Any, **kwargs: Any) -> int:  # pylint: disable=unused-argument
    print(inputdata)
    return 1


@utils.time_func
def part2(*args: Any, **kwargs: Any) -> int:  # pylint: disable=unused-argument
    return 0


if __name__ == "__main__":
    day_func_arguments = {}

    # Fixed test data
    inputdata = utils.get_day_data(1, test_data=True, **day_func_arguments)
    assert part1(silent=True) == 1  # type: ignore
    assert part2(silent=True) == 0  # type: ignore

    inputdata = utils.get_day_data(1, test_data=False, **day_func_arguments)
    utils.print_result(F'Part 1 answer: {part1()}')
    utils.print_result(F'Part 2 answer: {part2()}')
