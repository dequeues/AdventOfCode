from aoc import utils

inputdata = utils.get_day_data(2)

# mypy doesn't yet support match statements :-(
# https://github.com/python/mypy/pull/10191


def part1() -> int:
    horizontal, depth = 0, 0

    for course_command in inputdata:
        direction, str_amount = course_command.split(" ")
        amount = int(str_amount)
        if direction == "forward":
            horizontal += amount
        elif direction == "down":
            depth += amount
        else:
            depth -= amount

    return horizontal * depth


def part2() -> int:
    horizontal, depth, aim = 0, 0, 0

    for course_command in inputdata:
        direction, str_amount = course_command.split(" ")
        amount = int(str_amount)
        if direction == "forward":
            horizontal += amount
            depth += amount * aim
        elif direction == "down":
            aim += amount
        else:
            aim -= amount

    return horizontal * depth


utils.print_result(f"Part 1 answer: {part1()}")
utils.print_result(f"Part 2 answer: {part2()}")
