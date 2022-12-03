from aoc import utils


inputdata = utils.get_day_data(1, test_data=False, split_delimiter="\n\n")


@utils.time_func
def part1() -> int:
    elves: list[int] = []
    for elf in inputdata:
        elf_values_split = elf.split("\n")
        elves.append(sum(map(int, elf_values_split)))

    return max(elves)


@utils.time_func
def part2() -> int:
    return 0


utils.print_result(F'Part 1 answer: {part1()}')
utils.print_result(F'Part 2 answer: {part2()}')
