from aoc import utils


inputdata = utils.get_day_data(3, test_data=False)


@utils.time_func
def part1() -> int:
    rucksack_priorities: list[int] = []
    for rucksack in inputdata:
        compartment_one, compartment_two = set(
            rucksack[:len(rucksack)//2]), set(rucksack[len(rucksack)//2:])

        common_letter = next(iter(compartment_one & compartment_two))
        if common_letter.islower():
            rucksack_priorities.append(ord(common_letter)-96)
        else:
            rucksack_priorities.append((ord(common_letter.lower())-96)+26)

    return sum(rucksack_priorities)


@utils.time_func
def part2() -> int:
    return 0


utils.print_result(F'Part 1 answer: {part1()}')
utils.print_result(F'Part 2 answer: {part2()}')
