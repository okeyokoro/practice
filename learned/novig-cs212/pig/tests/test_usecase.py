import collections

from pig.entrypoint  import simulate
from pig.domain.strategies import clueless
from pig.domain.strategies import hold_at


def make_dieroll(array):
    q = collections.deque(array)

    def dieroll():
        return q.popleft()

    return dieroll


def test_dieroll_injection():

    dieroll = make_dieroll([1,2,3,4,5])

    assert dieroll() == 1
    assert dieroll() == 2
    assert dieroll() == 3
    assert dieroll() == 4
    assert dieroll() == 5


def test_start_with_player_1_winning():
    dieroll = make_dieroll([
        6, 6, 6, 6, 6, 6, 6, 6, 2, 4, 5
    ])

    assert 1 == simulate(hold_at(50), clueless, dieroll)


def test_player_can_start_game():
    assert 1 == 0

def test_player_can_take_turns():
    assert 1 == 0

def test_game_ends_when_someone_reaches_50():
    assert 1 == 0

def test_player_can_roll_die():
    assert 1 == 0

def test_players_score_keeps_getting_accumulated_as_they_roll_die():
    assert 1 == 0

def test_players_score_is_recorded_as_0_if_they_roll_a_1_and_it_becomes_the_next_players_turn():
    assert 1 == 0




