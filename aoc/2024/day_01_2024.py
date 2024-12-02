# pyright: strict, reportAny=false


import aoc.utils.core as utils

@utils.time_func
def part1(*args: str, **kwargs: int) -> int:  # pylint: disable=unused-argument # pyright: ignore[reportUnusedParameter]
    left, right = zip(*inputdata)
    left = sorted(left)
    right = sorted(right)

    distance: int = 0
    for l, r in zip(left, right):
        distance += abs(l - r)

    return distance



@utils.time_func
def part2(*args: str, **kwargs: int) -> int:  # pylint: disable=unused-argument # pyright: ignore[reportUnusedParameter]
    left, right = zip(*inputdata)
    similarity: int = 0
    for num in left:
        similarity += num * right.count(num)

    return similarity


day_func_arguments: utils.DaySettings = utils.DaySettings(line_format_func=lambda x: list(map(int, x.split())))


# Fixed test data
inputdata = utils.get_day_data(1, test_data=True, **day_func_arguments.model_dump(exclude={"test_data"}))
assert part1(silent=True) == 11  # type: ignore
assert part2(silent=True) == 31  # type: ignore

inputdata = utils.get_day_data(1, test_data=False, **day_func_arguments.model_dump(exclude={"test_data"}))
utils.print_result(F'Part 1 answer: {part1()}')
utils.print_result(F'Part 2 answer: {part2()}')
