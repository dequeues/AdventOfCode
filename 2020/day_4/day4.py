from re import match


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


def get_input_as_list() -> list[str]:
    with open('2020/day_4/input') as file:
        return [str(line.strip()) for line in file.read().split('\n\n')
                if line.strip()]


input_as_list = get_input_as_list()


def get_passports_dict_from_list() -> list[dict[str, str]]:
    passports: list[dict[str, str]] = []
    for line in input_as_list:
        line = line.replace('\n', ' ').replace(' ', ',')
        sections = line.split(',')
        keyval = [section.split(':') for section in sections]
        passports.append(
            dict([
                    (split[0], split[1]) for split in keyval
                    if len(split) == 2
            ])
        )
    return passports


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
