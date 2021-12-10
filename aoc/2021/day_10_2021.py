from dataclasses import dataclass
from statistics import median

from aoc import utils

inputdata = utils.get_day_data(10, test_data=False)


@dataclass
class CheckModel:
    score: int
    stack: list[str]


chars = {")": "(", "]": "[", "}": "{", ">": "<"}
scoring = {
    "a": {")": 3, "]": 57, "}": 1197, ">": 25137},
    "b": {"(": 1, "[": 2, "{": 3, "<": 4},
}


def part1() -> int:
    return sum([check(line).score for line in inputdata])


def part2() -> int:
    scores: list[int] = []
    for line in inputdata:
        check_result = check(line)

        if check_result.score != 0:
            continue

        score = 0
        for char in reversed(check_result.stack):
            score *= 5
            score += scoring["b"][char]

        scores.append(score)

    return int(median(scores))


def check(line) -> CheckModel:
    stack: list[str] = []
    for char in line:
        if char in chars.values():
            stack.append(char)
        else:
            if not stack or stack.pop() != chars[char]:
                return CheckModel(scoring["a"][char], stack)
    return CheckModel(0, stack)


print(f"Part 1 answer: {part1()}")
print(f"Part 2 answer: {part2()}")
