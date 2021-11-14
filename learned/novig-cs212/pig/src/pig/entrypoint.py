import random
import functools

from pig.domain.game import Game
from pig.domain.game import is_over

from pig.domain.strategies import clueless
from pig.domain.strategies import hold_at

from pig.usecase import play


def simulate(
    strategy1,
    strategy2,
    dieroll=functools.partial(random.randrange, start=1, stop=7)
):
    game = Game(
        current_player=1,
        player1_score=0,
        player2_score=0,
        pending_score=0,
        last_roll=None
    )

    player_strategy = {
        1: strategy1,
        2: strategy2,
    }

    while is_over(game) == False:
        rolled = dieroll()

        game = play(
            game,
            player_strategy[game.current_player](game),
            rolled,
        )

        print(game)

    return 1 if game.player1_score > game.player2_score else 2

if __name__ == "__main__":
    simulate(clueless, hold_at(20))

