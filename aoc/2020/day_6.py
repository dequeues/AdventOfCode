from collections import Counter
import common  # noqa pylint: disable=unused-import
import utils


inputlist = utils.get_day_data(6, '\n\n')


def part1() -> int:
    total: int = 0
    for group in [x.replace('\n', '') for x in inputlist]:
        total += len(Counter(group).keys())

    return total


def part2() -> int:
    total: int = 0
    for group in inputlist:
        letter_counter = Counter(group)
        people_count = len(group.split('\n'))
        answered_by_each_person = [
            x == people_count for x in letter_counter.values()
        ]
        total += sum(answered_by_each_person)

    return total


print(F'Part 1 answer: {part1()}')
print(F'Part 2 answer: {part2()}')
