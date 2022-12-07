from dataclasses import dataclass, field
from typing import Any, Union, Iterator
from aoc import utils

PART_TWO_REQUIRED_SIZE = 30000000
PART_TWO_TOTAL_SIZE = 70000000


@dataclass
class File:
    name: str
    size: int


@dataclass
class Directory:
    name: str
    parent: Union[None, "Directory"] = None
    size: int = 0
    children_nodes: list[Union[File, "Directory"]] = field(default_factory=list)

    def get_directory(self, directory_name: str) -> "Directory":
        if self.name == directory_name and directory_name == "/":
            return self

        if directory_name == "..":
            if self.parent:
                return self.parent
            return self

        for node in self.children_nodes:
            if isinstance(node, Directory) and node.name == directory_name:
                return node
        raise AttributeError(
            (
                f"{directory_name} not found "
                f"(parent: {self.parent.name if self.parent else 'none'})"
            )
        )

    def __iter__(self) -> Iterator[Union[File, "Directory"]]:
        return iter(self.children_nodes)


def get_sum_of_directories_with_max_size(tree: Directory, max_size: int) -> int:
    total = 0
    for directory in tree.children_nodes:
        if isinstance(directory, Directory):
            if directory.size < max_size:
                total += directory.size
            if len(directory.children_nodes) > 0:
                total += get_sum_of_directories_with_max_size(directory, max_size)
    return total


def get_all_directories(tree: Directory) -> list[Directory]:
    directory_list = []
    for directory in tree:
        if isinstance(directory, Directory):
            inner_list = get_all_directories(directory)
            if len(inner_list) > 0:
                directory_list += inner_list

            directory_list.append(directory)
    return directory_list


def create_directory_tree() -> Directory:
    directory = Directory(name="/", children_nodes=[])

    current_command_group: Union[None, str] = None
    current_directory = directory
    for line in inputdata:
        if line[0] == "$":
            line = line[2:]
            command_parts = line.split(" ")
            current_command_group = line
            if command_parts[0] == "cd":
                current_directory = current_directory.get_directory(
                    command_parts[1])
                continue
            if current_command_group == "ls":
                continue

        command, arg = line.split(" ")

        if current_command_group == "ls":
            if command == "dir":
                current_directory.children_nodes.append(
                    Directory(
                        name=arg,
                        children_nodes=[],
                        parent=current_directory
                    )
                )
            else:
                current_directory.size += int(command)
                cur = current_directory
                while cur.parent:
                    cur.parent.size += int(command)
                    cur = cur.parent
                current_directory.children_nodes.append(
                    File(name=arg, size=int(command)))
            continue
    return directory


@ utils.time_func
def part1(*args: Any, **kwargs: Any) -> int:  # pylint: disable=unused-argument
    directory = create_directory_tree()
    return get_sum_of_directories_with_max_size(directory, 100000)


@ utils.time_func
def part2(*args: Any, **kwargs: Any) -> int:  # pylint: disable=unused-argument
    directory = create_directory_tree()
    directories_sorted = sorted(get_all_directories(directory), key=lambda x: x.size)
    for inner_directory in directories_sorted:
        free_space = PART_TWO_TOTAL_SIZE - (directory.size - inner_directory.size)
        if free_space >= PART_TWO_REQUIRED_SIZE:
            return inner_directory.size

    return 0


# Fixed test data
inputdata = utils.get_day_data(7, test_data=True)
assert part1(silent=True) == 95437  # type: ignore
assert part2(silent=True) == 24933642  # type: ignore

inputdata = utils.get_day_data(7, test_data=False)
utils.print_result(F'Part 1 answer: {part1()}')
utils.print_result(F'Part 2 answer: {part2()}')
