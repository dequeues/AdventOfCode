from re import findall
from typing import Any

import aoc.utils.core as utils


@utils.time_func
def part1(*args: Any, **kwargs: Any) -> int:  # pylint: disable=unused-argument
    total: int = 0
    for line in inputdata:
        current_number: int = 0
        digits = findall(r"\d", line)
        if len(digits) > 1:
            current_number = int(digits[0] + digits[-1])
        else:
            current_number = int(digits[0] + digits[0])
        total += current_number

    return total


@utils.time_func
def part2(*args: Any, **kwargs: Any) -> int:  # pylint: disable=unused-argumenti
    numbers: dict[str, str] = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    total: int = 0

    for line in inputdata:
        digits = findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)
        value = "".join(numbers[d] if d.isalpha() else d for d in [digits[0], digits[-1]])
        total += int(value)

    return total


day_func_arguments: dict[str, Any] = {
    "split_delimiter": "\n"
}

# Fixed test data
inputdata = utils.get_day_data(1, test_data=True, **day_func_arguments)
assert part1(silent=True) == 142  # type: ignore
inputdata = utils.get_day_data(1, test_data=True, part_two = True, **day_func_arguments)
assert part2(silent=True) == 281  # type: ignore

inputdata = utils.get_day_data(1, test_data=False, **day_func_arguments)
utils.print_result(F'Part 1 answer: {part1()}')
utils.print_result(F'Part 2 answer: {part2()}')
