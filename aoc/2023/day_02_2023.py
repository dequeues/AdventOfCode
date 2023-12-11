import math
import re
from dataclasses import asdict, dataclass
from typing import Any

import aoc.utils.core as utils


@dataclass
class Game:
    blue: int = 0
    green: int = 0
    red: int = 0
    dict = asdict

    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, item, value):
        return setattr(self, item, value)


def setup(requirements: Game):
    games: list[Game] = []
    for line in inputdata:
        parts = re.sub("[;,:]", "", line).split()
        game_score = Game()
        for count, color in zip(parts[2::2], parts[3::2]):
            game_score[color] = max(game_score[color], int(count))
        games.append(game_score)

    return games


@utils.time_func
def part1(*args: Any, **kwargs: Any) -> int:  # pylint: disable=unused-argument
    games = setup(kwargs.get("requirements"))
    requirements: Game = kwargs.get("requirements")
    successful_games: list[int] = []
    for idx, game_score in enumerate(games):
        if all(
            [
                game_score.red <= requirements.red,
                game_score.green <= requirements.green,
                game_score.blue <= requirements.blue,
            ]
        ):
            successful_games.append(idx + 1)

    return sum(successful_games)


@utils.time_func
def part2(*args: Any, **kwargs: Any) -> int:  # pylint: disable=unused-argument
    games = setup(kwargs.get("requirements"))

    total_power = 0
    for game in games:
        total_power += math.prod(game.dict().values())

    return total_power


day_func_arguments: dict[str, Any] = {}

# Fixed test data
inputdata = utils.get_day_data(2, test_data=True, **day_func_arguments)
assert part1(silent=True, requirements=Game(red=12, green=13, blue=14)) == 8  # type: ignore
assert part2(silent=True, requirements=Game(red=12, green=13, blue=14)) == 2286  # type: ignore

inputdata = utils.get_day_data(2, test_data=False, **day_func_arguments)
utils.print_result(
    f"Part 1 answer: {part1(requirements=Game(red=12, green=13, blue=14))}"
)
utils.print_result(f"Part 2 answer: {part2()}")
