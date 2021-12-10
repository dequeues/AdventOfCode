import numpy as np

from aoc import utils


inputdata = utils.get_day_data(7, test_data=False, split_delimiter=",")


def part1() -> int:
    crabs = list(map(int, inputdata.copy()))

    median = np.round(np.median(crabs))

    return int(sum([np.abs(median - x) for x in crabs]))


def part2() -> int:
    data = list(map(int, inputdata.copy()))

    mean = int(np.mean(data))

    return int(
        sum(np.abs(x - mean) * (np.abs(x - mean) + 1) // 2 for x in data)
    )


utils.print_result(f"Part 1 answer: {part1()}")
print(f"Part 2 answer: {part2()}")
