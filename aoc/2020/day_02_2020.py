import re

from aoc import utils


def format_input(input_data: list[str]) -> list[tuple[int, int, str, str]]:
    outlist: list[tuple[int, int, str, str]] = []
    part_re = re.compile("([0-9]+)-([0-9]+) ([a-zA-Z]): ([a-zA-Z]+)")
    for line in input_data:
        split = part_re.match(line)
        if split:
            outlist.append(
                (
                    int(split.group(1)),
                    int(split.group(2)),
                    str(split.group(3)),
                    str(split.group(4)),
                )
            )
    return outlist


input_list: list[str] = utils.get_day_data(2)
formatted_input = format_input(input_list)


def part1() -> int:
    valid_passwords: int = 0
    for tup in formatted_input:
        password_min, password_max, password_char, password = tup
        charcount: int = password.count(password_char)
        if password_max >= charcount >= password_min:
            valid_passwords += 1

    return valid_passwords


def part2() -> int:
    valid_passwords: int = 0
    for tup in formatted_input:
        password_min, password_max, password_char, password = tup
        if (password[password_min - 1] == password_char) ^ (
            password[password_max - 1] == password_char
        ):
            valid_passwords += 1

    return valid_passwords


utils.print_result(f"Part 1 answer: {part1()}")
utils.print_result(f"Part 2 answer: {part2()}")
