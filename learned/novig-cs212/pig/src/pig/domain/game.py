import copy
import dataclasses


goal = 50

other_player = {
    1: 2,
    2: 1
}

player_score = {
    1: "player1_score",
    2: "player2_score",
}


@dataclasses.dataclass
class Game:
    player1_score:  int
    player2_score:  int
    current_player: int # 1 or 2
    pending_score:  int
    last_roll:      int # 0 will indicate hold


def roll(game: Game, rolled:int):
    if rolled == 1:
        current_player_score = player_score[game.current_player]

        new_game = copy.copy(game)
        new_game.last_roll = rolled
        new_game.pending_score = 0
        new_game.current_player = other_player[
            game.current_player
        ]

        setattr(
            new_game,
            current_player_score,
            getattr(game, current_player_score) + 1
        )

        return new_game

    return Game(
        player1_score=game.player1_score,
        player2_score=game.player2_score,
        current_player=game.current_player,
        pending_score=game.pending_score + rolled,
        last_roll=rolled,
    )

def hold(game: Game):
    add = {
        1 : game.pending_score if game.current_player == 1 else 0,
        2 : game.pending_score if game.current_player == 2 else 0,
    }
    return Game(
        last_roll=0,
        pending_score=0,
        player1_score=game.player1_score + add[1],
        player2_score=game.player2_score + add[2],
        current_player=other_player[
            game.current_player
        ],
    )

def is_over(game: Game):
    if game.player1_score >= goal:
        return True
    if game.player2_score >= goal:
        return True
    return False

