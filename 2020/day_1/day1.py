def get_input_as_list() -> list[int]:
    with open('2020/day_1/input') as file:
        return [int(line.strip()) for line in file.read().split('\n')]


input = get_input_as_list()


def part1() -> int:
    for i in input:
        for j in input:
            if (i + j == 2020):
                return (i * j)
    return 0


def part2() -> int:
    for i in input:
        for j in input:
            for k in input:
                if (i + j + k == 2020):
                    return (i * j * k)
    return 0


print(F'Part 1 answer: {part1()}')
print(F'Part 2 answer: {part2()}')
