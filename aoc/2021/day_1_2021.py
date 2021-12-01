from aoc import utils

inputdata = list(map(int, utils.get_day_data(1)))


def part1() -> int:
    return sum(
        1 for i in range(1, len(inputdata)) if inputdata[i - 1] < inputdata[i]
    )


def part2() -> int:
    total_by_window_groups = [
        sum(inputdata[i : i + 3]) for i in range(len(inputdata))
    ]
    return sum(
        1
        for i in range(len(total_by_window_groups) - 1)
        if total_by_window_groups[i + 1] > total_by_window_groups[i]
    )


print(f"Part 1 answer: {part1()}")
print(f"Part 2 answer: {part2()}")
