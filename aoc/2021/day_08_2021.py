from itertools import permutations

from aoc import utils


inputdata = utils.get_day_data(
    8, test_data=False, line_format_func=lambda x: x.split(" | ")
)

combinations: dict[str, int] = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}


def part1() -> int:
    data = inputdata.copy()

    return_no = 0
    for line in data:
        _, output_data = line[0].split(" "), line[1].split(" ")
        return_no += sum(len(code) in [2, 3, 4, 7] for code in output_data)

    return return_no


def part2() -> int:
    data = inputdata.copy()

    return_no = 0
    for line in data:
        input_data, output_data = line[0].split(" "), line[1].split(" ")
        for permutation in permutations("abcdefg"):
            ascii_combination = str.maketrans("abcdefg", "".join(permutation))
            input_combinations, output_combinations = [
                "".join(sorted(code.translate(ascii_combination)))
                for code in input_data
            ], [
                "".join(sorted(code.translate(ascii_combination)))
                for code in output_data
            ]

            if all(code in combinations for code in input_combinations):
                return_no += int(
                    "".join(
                        str(combinations[code]) for code in output_combinations
                    )
                )
                break

    return return_no


print(f"Part 1 answer: {part1()}")
print(f"Part 2 answer: {part2()}")
