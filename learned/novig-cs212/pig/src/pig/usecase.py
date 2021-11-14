import functools

from pig.domain.game import roll
from pig.domain.game import hold


def play(game, action, rolled):
    action_map = {
        "roll": functools.partial(roll, rolled=rolled),
        "hold": hold
    }

    return action_map[action](game)

