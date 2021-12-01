import re

from aoc import utils


BAG_RULE = re.compile(r"(\d+) ([\w ]+) bag")
BAG_COLOR = "shiny gold"

inputlist: list[str] = utils.get_day_data(7)


def get_tree(data: list[str]) -> dict[str, list[tuple[int, str]]]:
    rules = {}
    for line in data:
        color, contents = line.split(" bags contain ")
        bag_content = BAG_RULE.findall(contents)
        rules[color] = [(int(n), inner) for n, inner in bag_content]

    return rules


def count_bags_of(target, tree) -> int:
    count = 0
    for color in tree:
        if has_bag(color, target, tree):
            count += 1
    return count


def has_bag(color, target, tree) -> bool:
    contents = tree[color]
    return any(
        inner == target or has_bag(inner, target, tree)
        for _, inner in contents
    )


def count_bags_inside(color, tree) -> int:
    contents = tree[color]
    return sum(
        n * (1 + count_bags_inside(inner, tree)) for n, inner in contents
    )


def part1(tree) -> int:
    return count_bags_of(BAG_COLOR, tree)


def part2(tree) -> int:
    return count_bags_inside(BAG_COLOR, tree)


trees = get_tree(inputlist)

print(f"Part 1 answer: {part1(trees)}")
print(f"Part 2 answer: {part2(trees)}")
