from re import sub
from typing import Union

import numpy as np

from aoc import utils


inputdata = utils.get_day_data(4, "\n")


def part1() -> int:
    drawn_numbers, cards = process_and_get_input()
    for drawn in drawn_numbers:
        cards = np.where(cards == drawn, np.nan, cards)
        states = np.array([does_board_have_a_winner(board) for board in cards])
        if np.any(states):
            return int(np.nansum(cards[np.argmax(states)]) * drawn)

    return 0


def part2() -> int:
    drawn_numbers, cards = process_and_get_input()
    last = -1
    for drawn in drawn_numbers:
        cards = np.where(cards == drawn, np.nan, cards)
        states = np.array([does_board_have_a_winner(board) for board in cards])
        if np.count_nonzero(~states) == 1:
            last = int(np.argmin(states))

        if last > -1 and states[last]:
            return int(np.nansum(cards[last]) * drawn)

    return 0


def process_and_get_input() -> tuple[np.ndarray, np.ndarray]:
    numbers_pulled = np.array(list(map(int, inputdata[0].split(","))))
    raw_cards = list(
        inputdata[x : x + 5] for x in range(1, len(inputdata[1:]), 5)
    )
    card_matrixes: list[list[Union[int, np.ndarray]]] = [[0]] * (
        len(raw_cards)
    )

    for idx, card in enumerate(raw_cards):
        card_matrixes[idx] = []
        for numbers in card:
            numbers = sub(r"\s{2,}", " ", numbers)
            card_matrixes[idx].append(
                np.array(list(map(int, numbers.split(" "))), dtype=int)
            )

    return numbers_pulled, np.array(card_matrixes)


def does_board_have_a_winner(board: np.ndarray) -> np.bool_:
    board_matrix = np.reshape(board, (5, 5))
    return np.any(
        [
            [np.isnan(board_matrix[i]).all() for i in range(5)],
            [np.isnan(board_matrix.transpose()[i]).all() for i in range(5)],
        ]
    )


print(f"Part 1 answer: {part1()}")
print(f"Part 2 answer: {part2()}")
