import aoc.utils.core as utils


def is_safe_report(report: list[int]) -> bool:
    """Check if a report is safe based on the rules."""
    differences = [abs(b - a) for a, b in zip(report, report[1:])]

    return all(1 <= diff <= 3 for diff in differences) and (
        all(report[i] >= report[i + 1] for i in range(len(report) - 1))
        or all(report[i] <= report[i + 1] for i in range(len(report) - 1))
    )


def is_safe_with_dampener(report: list[int]) -> bool:
    if is_safe_report(report):
        return True

    for i in range(len(report)):
        modified = report[:i] + report[i + 1 :]
        if is_safe_report(modified):
            return True

    return False


@utils.time_func
def part1(*args: str, **kwargs: int) -> None | int:  # pylint: disable=unused-argument # pyright: ignore[reportUnusedParameter]
    res = sum(1 for report in inputdata if is_safe_report(report))  # pyright: ignore[reportArgumentType]
    return res


@utils.time_func
def part2(*args: str, **kwargs: int) -> None | int:  # pylint: disable=unused-argument # pyright: ignore[reportUnusedParameter]
    return sum(1 for report in inputdata if is_safe_with_dampener(report))  # pyright: ignore[reportArgumentType]


day_func_arguments: utils.DaySettings = utils.DaySettings(
    line_format_func=lambda x: list(map(int, x.split()))
)

# Fixed test data
inputdata = utils.get_day_data(2, test_data=True, day_settings=day_func_arguments)
assert part1(silent=True) == 2
assert part2(silent=True) == 4

inputdata = utils.get_day_data(2, test_data=False, day_settings=day_func_arguments)
part_one_result = part1()
part_two_result = part2()
utils.print_result(f"Part 1 answer: {part_one_result}")
utils.print_result(f"Part 2 answer: {part_two_result}")
