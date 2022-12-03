from aoc import utils


inputdata = utils.get_day_data(1, test_data=False, split_delimiter="\n\n")

elves: list[int] = []
for elf in inputdata:
    elf_values_split = elf.split("\n")
    elves.append(sum(map(int, elf_values_split)))


@utils.time_func
def part1() -> int:
    return max(elves)


@utils.time_func
def part2() -> int:
    elves_sorted = sorted(elves)
    return sum(elves_sorted[-3:])


utils.print_result(F'Part 1 answer: {part1()}')
utils.print_result(F'Part 2 answer: {part2()}')
