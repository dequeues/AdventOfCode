from aoc import utils

inputdata = utils.get_day_data(8)


def process_instruction_string(instruction: str) -> tuple[str, int]:
    operation, argument = instruction.split()
    return (operation, int(argument))


def process_instructions(instructions: list[str]) -> tuple[int, bool]:
    accumulator: int = 0
    ran_instructions: set[int] = set()

    i = 0
    while i not in ran_instructions:
        if i == len(instructions):
            return (accumulator, True)

        operation, argument = process_instruction_string(instructions[i])

        ran_instructions.add(i)
        if operation == "acc":
            accumulator += int(argument)
            i += 1
        elif operation == "jmp":
            i += int(argument)
        elif operation == "nop":
            i += 1

    return (accumulator, False)


def part1() -> int:
    return process_instructions(inputdata)[0]


def part2() -> int:
    for i, instruction in enumerate(inputdata):
        operation, _ = process_instruction_string(instruction)
        if operation in ["jmp", "nop"]:
            new_instructions = inputdata.copy()
            new_instructions[i] = instruction.replace(
                operation, "jmp" if operation == "nop" else "nop"
            )
            accumulator, completed = process_instructions(new_instructions)
            if completed:
                return accumulator

    return 0


utils.print_result(f"Part 1 answer: {part1()}")
utils.print_result(f"Part 2 answer: {part2()}")
