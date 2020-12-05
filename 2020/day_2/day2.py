import re


def get_input_as_list() -> list[str]:
    with open('2020/day_2/input') as file:
        return [str(line.strip()) for line in file.read().split('\n')]


def format_input(input: list[str]) -> list[tuple[int, int, str, str]]:
    outlist: list[tuple[int, int, str, str]] = []
    part_re = re.compile('([0-9]+)-([0-9]+) ([a-zA-Z]): ([a-zA-Z]+)')
    for line in input:
        split = part_re.match(line)
        if split:
            outlist.append((
                int(split.group(1)),
                int(split.group(2)),
                str(split.group(3)),
                str(split.group(4))
            ))
    return outlist


formatted_input = format_input(get_input_as_list())


def part1() -> int:
    valid_passwords: int = 0
    for tup in formatted_input:
        password_min, password_max, password_char, password = tup
        charcount: int = password.count(password_char)
        if charcount >= password_min and charcount <= password_max:
            valid_passwords += 1

    return valid_passwords


def part2() -> int:
    valid_passwords: int = 0
    for tup in formatted_input:
        password_min, password_max, password_char, password = tup
        if (
            (password[password_min - 1] == password_char) ^
            (password[password_max - 1] == password_char)
        ):
            valid_passwords += 1

    return valid_passwords


print(F'Part 1 answer: {part1()}')
print(F'Part 2 answer: {part2()}')
