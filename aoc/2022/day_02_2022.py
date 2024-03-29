from enum import Enum
from aoc import utils

inputdata = utils.get_day_data(2, test_data=False)


class TypeScores(Enum):
    ROCK: int = 1
    PAPER: int = 2
    SCISSORS: int = 3


class RPSRoundScoring(Enum):
    LOSS = 0
    DRAW = 3
    WIN = 6


TURN_OPTIONS = ["ROCK", "PAPER", "SCISSORS"]


def get_turn(turn_char: str) -> str:
    if turn_char in ["A", "X"]:
        return "ROCK"
    elif turn_char in ["B", "Y"]:
        return "PAPER"
    else:
        return "SCISSORS"


@utils.time_func
def part1() -> int:
    my_score: int = 0
    for game_round in inputdata:
        opponent_turn, my_turn = map(get_turn, game_round.split(" "))

        my_score += TypeScores[my_turn].value
        if opponent_turn == my_turn:
            my_score += RPSRoundScoring.DRAW.value
        else:
            my_outcome = "WIN" if TURN_OPTIONS[(TURN_OPTIONS.index(
                opponent_turn) + 1) % 3] == my_turn else "LOSS"
            my_score += RPSRoundScoring[my_outcome].value
    return my_score


@utils.time_func
def part2() -> int:
    my_score: int = 0
    desired_outcomes_str = {"X": RPSRoundScoring.LOSS,
                            "Y": RPSRoundScoring.DRAW, "Z": RPSRoundScoring.WIN}
    for game_round in inputdata:
        opponent_turns = game_round.split(" ")
        opponent_turn, desired_outcome = get_turn(
            opponent_turns[0]), desired_outcomes_str[opponent_turns[1]]

        my_score += desired_outcome.value
        if desired_outcome == RPSRoundScoring.DRAW:
            my_score += TypeScores[opponent_turn].value

        elif desired_outcome == RPSRoundScoring.LOSS:
            my_score += TypeScores[TURN_OPTIONS[TURN_OPTIONS.index(
                opponent_turn) - 1]].value
        else:
            my_score += TypeScores[TURN_OPTIONS[(TURN_OPTIONS.index(
                opponent_turn) + 1) % 3]].value

    return my_score


utils.print_result(F'Part 1 answer: {part1()}')
utils.print_result(F'Part 2 answer: {part2()}')
