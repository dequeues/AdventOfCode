import numpy as np

from aoc import utils

input_data = utils.get_day_data(9, test_data=False)

heightmap = np.array([list(line) for line in input_data], dtype=int)
low_adj = []
low_points = []


def part1() -> int:
    for i in range(heightmap.shape[0]):
        for j in range(heightmap.shape[1]):
            if get_window_max([i, j], heightmap):
                low_adj.append(heightmap[i][j] + 1)
                low_points.append([i, j])
    return sum(low_adj)


def part2() -> int:
    basins = []
    for loc_min in low_points:
        data = heightmap.copy()

        flood_fill(data, loc_min[0], loc_min[1])

        basin = data == 10
        basin_size = len(data[basin])
        basins.append(basin_size)
        top_3_basins = sorted(basins)[-3:]
    return top_3_basins[0] * top_3_basins[1] * top_3_basins[2]


def get_window_max(coords, arr):
    local_min = False
    if coords[0] == 0:
        top = arr[coords[0]][coords[1]]
    else:
        top = arr[coords[0] - 1][coords[1]]
    if coords[0] == arr.shape[0] - 1:
        bot = arr[coords[0]][coords[1]]
    else:
        bot = arr[coords[0] + 1][coords[1]]
    if coords[1] == 0:
        left = arr[coords[0]][coords[1]]
    else:
        left = arr[coords[0]][coords[1] - 1]
    if coords[1] == arr.shape[1] - 1:
        right = arr[coords[0]][coords[1]]
    else:
        right = arr[coords[0]][coords[1] + 1]

    adj = arr[coords[0]][coords[1]]
    if adj == top == bot == left == right:
        pass
    elif min(adj, top, bot, left, right) == adj:
        local_min = True

    return local_min


def flood_fill(data, row, col):
    row_max, col_max = data.shape
    if row < 0 or col < 0 or row >= row_max or col >= col_max:
        return
    if data[row][col] == 9 or data[row][col] == 10:
        return
    data[row][col] = 10
    flood_fill(data, row, col + 1)
    flood_fill(data, row, col - 1)
    flood_fill(data, row + 1, col)
    flood_fill(data, row - 1, col)


utils.print_result(f"Part 1 answer: {part1()}")
utils.print_result(f"Part 2 answer: {part2()}")
