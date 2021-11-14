import random
import functools

from pig.domain.game import goal
from pig.domain.game import player_score
from pig.domain.game import Game
from pig.domain.game import hold
from pig.domain.game import roll

"""The point of a strategy
    is to determine whether a player should 'hold' or 'roll' given the game state
"""

def clueless(_):
    return random.choice(["roll", "hold"])

def hold_at(x: int):
    """hold_at is a factory function
        that manufactures hold_at strategies
    """
    def strategy(game: Game):
        """a hold_at strategy will
            roll untill it reaches a certain value x, form that point on it will hold
        """
        if game.pending_score >= x:
            return "hold"

        im_winning = (
            game.pending_score + getattr(game, player_score[game.current_player])
            >= goal
        )
    
        if game.pending_score > 0 and im_winning:
            return "hold"

        return "roll"

    strategy.__name__ = f"hold_at({x})"
    return strategy

def optimal(game):

    def Q_pig(state, action, Pwin):
        """The quality of a state"""
        if action == "hold":
            new_state = hold(state)
            Pwin_opponent = Pwin(new_state)
            return 1 - Pwin_opponent

        if action == "roll":
            rolled_1_state = roll(state, 1)
            Pwin_opponent = Pwin(rolled_1_state)
            Pat_rolled_1 = 1 - Pwin_opponent
            otherPs = [ Pwin(roll(state, x)) for x in (2,3,4,5,6) ]
            return (Pat_rolled_1 + sum(otherPs)) / 6

    def pig_actions(state):
        return [ "roll", "hold" ] if state.pending_score else [ "roll" ]

    # @functools.lru_cache
    def Pwin(state):
        """The utility of a state is the probability of winning """
        me = state.player1_score if state.current_player == 1 else state.player2_score
        you = state.player2_score if state.current_player == 1 else state.player1_score

        if me + state.pending_score >= goal:
            return 1
        elif you >= goal:
            return 0
        else:
            return max(
                Q_pig(state, action, Pwin) # recursion...
                for action in pig_actions(state)
            )

    if Q_pig(game, "roll", Pwin) > Q_pig(game, "hold", Pwin):
        return "roll"

    return "hold"
