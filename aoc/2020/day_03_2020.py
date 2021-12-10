from aoc import utils


SQUARE, TREE = (".", "#")

input_list: list[str] = utils.get_day_data(3)


def get_trees_in_slope(d_x: int, d_y: int) -> int:
    cur_x, cur_y, trees, length, width = (
        0,
        0,
        0,
        len(input_list) - d_y,
        len(input_list[0]),
    )

    while cur_y < length:
        cur_x = (cur_x + d_x) % width
        cur_y += d_y
        if input_list[cur_y][cur_x] == TREE:
            trees += 1

    return trees


def part1():
    return get_trees_in_slope(3, 1)


def part2(part1_trees: int) -> int:
    moves: list[list[int]] = [[1, 1], [5, 1], [7, 1], [1, 2]]
    trees: int = part1_trees
    for move in moves:
        trees *= get_trees_in_slope(move[0], move[1])

    return trees


PART1_TREES = part1()
utils.print_result(f"Part 1 answer: {PART1_TREES}")
utils.print_result(f"Part 2 answer: {part2(PART1_TREES)}")
