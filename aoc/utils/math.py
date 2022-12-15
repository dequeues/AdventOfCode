def manhattan_distance(point_a: tuple[int, ...], point_b: tuple[int, ...]) -> int:
    return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])
