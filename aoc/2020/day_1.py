import common  # noqa pylint: disable=unused-import
import utils

input_list: list[int] = utils.convert_list_to_ints(utils.get_day_data(1))


def part1() -> int:
    for i in input_list:
        for j in input_list:
            if i + j == 2020:
                return i * j
    return 0


def part2() -> int:
    for i in input_list:
        for j in input_list:
            for k in input_list:
                if i + j + k == 2020:
                    return i * j * k
    return 0


print(F'Part 1 answer: {part1()}')
print(F'Part 2 answer: {part2()}')
