# Squares = .
# Trees = #
SQUARE, TREE = ('.', '#')


def get_input_as_list() -> list[str]:
    with open('2020/day_3/input') as file:
        return [str(line.strip()) for line in file.read().split('\n') if line]


input = get_input_as_list()


def get_trees_in_slope(dx: int, dy: int) -> int:
    cur_x, cur_y, trees, length, width = (
        0,
        0,
        0,
        len(input) - dy,
        len(input[0])
    )

    while cur_y < length:
        cur_x = (cur_x + dx) % width
        cur_y += dy
        if input[cur_y][cur_x] == TREE:
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


part1_trees = part1()
print(F'Part 1 answer: {part1_trees}')
print(F'Part 2 answer: {part2(part1_trees)}')
