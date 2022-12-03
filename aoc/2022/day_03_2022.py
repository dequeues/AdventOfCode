from aoc import utils


inputdata = utils.get_day_data(3, test_data=False)


def get_priority(letter: str) -> int:
    if letter.islower():
        return ord(letter)-96
    return (ord(letter.lower())-96)+26


@ utils.time_func
def part1() -> int:
    rucksack_priorities: list[int] = []
    for rucksack in inputdata:
        compartment_one, compartment_two = set(
            rucksack[:len(rucksack)//2]), set(rucksack[len(rucksack)//2:])

        common_letter = next(iter(compartment_one & compartment_two))
        rucksack_priorities.append(get_priority(common_letter))

    return sum(rucksack_priorities)


@ utils.time_func
def part2() -> int:
    rucksack_priorities: list[int] = []
    groups = [inputdata[i:i+3] for i in range(0, len(inputdata), 3)]

    for group in groups:
        common_letter = next(iter(set(group[0]) & set(group[1]) & set(group[2])))
        rucksack_priorities.append(get_priority(common_letter))

    return sum(rucksack_priorities)


utils.print_result(F'Part 1 answer: {part1()}')
utils.print_result(F'Part 2 answer: {part2()}')
