from collections import Counter

from aoc import utils

inputdata = utils.get_day_data(14, test_data=False)


def get_common_data() -> tuple[dict[str, str], Counter[str], Counter[str]]:
    template = inputdata[0]
    rules = {x.split(" -> ")[0]: x.split(" -> ")[1] for x in inputdata[1:]}
    pairs = Counter(map(str.__add__, template, template[1:]))
    chars = Counter(template)
    return rules, pairs, chars


def simulate(
    steps: int,
    rules: dict[str, str],
    pairs: dict[str, int],
    chars: Counter[str],
) -> int:
    for _ in range(steps):
        for rule_chars, count in pairs.copy().items():
            char_1 = rule_chars[0]
            char_2 = rule_chars[1]
            idx = rules[char_1 + char_2]
            pairs[char_1 + char_2] -= count
            pairs[char_1 + idx] += count
            pairs[idx + char_2] += count
            chars[idx] += count

    return max(chars.values()) - min(chars.values())


@utils.time_func
def part1() -> int:
    return simulate(10, *get_common_data())


@utils.time_func
def part2() -> int:
    return simulate(40, *get_common_data())


utils.print_result(f"Part 1 answer: {part1()}")
utils.print_result(f"Part 2 answer: {part2()}")
