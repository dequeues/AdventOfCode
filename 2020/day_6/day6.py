from collections import Counter


def get_input_as_list() -> list[str]:
    with open('2020/day_6/input') as file:
        return [str(line.strip()) for line in file.read().split('\n\n')
                if line.strip()]


inputlist = get_input_as_list()


def part1() -> int:
    total: int = 0
    for group in [x.replace('\n', '') for x in inputlist]:
        total += len(Counter(group).keys())

    return total


def part2():
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
