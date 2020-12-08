from re import match
import common  # noqa pylint: disable=unused-import
import utils


REQUIRED_FIELDS = {
    'byr': (lambda n: int(n) and len(n) == 4 and 1920 <= int(n) <= 2002),
    'iyr': (lambda n: int(n) and len(n) == 4 and 2010 <= int(n) <= 2020),
    'eyr': (lambda n: int(n) and len(n) == 4 and 2020 <= int(n) <= 2030),
    'hgt': (lambda n: int(n[:-2]) and n[-2:] in ['cm', 'in'] and (
        (n[-2:] == 'cm' and 150 <= int(n[:-2]) <= 193) or
        (n[-2:] == 'in' and 59 <= int(n[:-2]) <= 76)
    )),
    'hcl': (lambda n: len(n) == 7 and match('#[0-9a-f]{6}', n)),
    'ecl': (lambda n: n in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']),
    'pid': (lambda n: int(n) and len(n) == 9),
}

input_as_list = utils.get_day_data(4, '\n\n')


def get_passports_dict_from_list() -> list[dict[str, str]]:
    passport_list: list[dict[str, str]] = []
    for line in input_as_list:
        line = line.replace('\n', ' ').replace(' ', ',')
        sections = line.split(',')
        keyval = [section.split(':') for section in sections]
        passport_list.append(dict((key, value) for (key, value) in keyval))

    return passport_list


def has_all_required_fields(passport: dict[str, str]) -> bool:
    return all(field in passport for field in REQUIRED_FIELDS)


passports = get_passports_dict_from_list()


def part1() -> int:
    valids = [val for val in passports if has_all_required_fields(val)]
    return len(valids)


def part2() -> int:
    count: int = 0
    for passport in passports:
        for field, validator in REQUIRED_FIELDS.items():
            if field not in passport.keys():
                break

            try:
                if not validator(passport[field]):
                    break
            except ValueError:
                break

        else:
            count += 1

    return count


print(F'Part 1 answer: {part1()}')
print(F'Part 2 answer: {part2()}')
