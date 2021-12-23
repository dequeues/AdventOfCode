from aoc import utils


inputdata = utils.get_day_data(13, test_data=False)


def get_working_data() -> tuple[set[tuple[int, ...]], list[tuple[str, int]]]:
    coords = set()
    instructions = []
    for line in inputdata:
        if "," in line:
            coords.add(tuple(map(int, line.split(","))))
        elif "=" in line:
            axis = line.split(" ")[-1].split("=")[0]
            fold_pos = int(line.split(" ")[-1].split("=")[-1])
            instructions.append((axis, fold_pos))

    return coords, instructions


def do_fold(
    coords: set[tuple[int, ...]], axis: str, position: int
) -> set[tuple[int, ...]]:
    if axis == "x":
        return set(
            [
                (x - (2 * (x - position)), y) if x > position else (x, y)
                for x, y in coords
            ]
        )
    return set(
        [
            (x, y - (2 * (y - position))) if y > position else (x, y)
            for x, y in coords
        ]
    )


COORDS, INSTRUCTIONS = get_working_data()


@utils.time_func
def part1() -> int:
    return len(do_fold(COORDS, INSTRUCTIONS[0][0], INSTRUCTIONS[0][1]))


@utils.time_func
def part2() -> str:
    coords = COORDS
    for instruction in INSTRUCTIONS:
        coords = do_fold(coords, instruction[0], instruction[1])

    out: list[str] = []

    for x in range(7):  # pylint: disable=invalid-name
        out.append("")
        for y in range(40):  # pylint: disable=invalid-name
            if (y, x) in coords:
                out[x] += "#"
            else:
                out[x] += " "

    return "\n".join(out)


utils.print_result(f"Part 1 answer: {part1()}")
utils.print_result(f"Part 2 answer: \n{part2()}")
