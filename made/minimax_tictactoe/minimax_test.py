import copy

import pytest

from minimax import Board
from minimax import Node


class TestBoard():

    def test_who_won(self):
        board = [
            ["T", None, None],
            [None, "T", None],
            [None, None, "T"],
        ]

        assert Board.who_won(board) == "T"

    @pytest.mark.xfail
    def test_who_won_bad(self):
        board = [
            ["T",  None, None],
            [None, None, None],
            [None, None, "T"],
        ]

        assert Board.who_won(board) == "T"


class TestNode():

    def test_next_stage(self):
        board = [
            #  0     1     2   col/row
            ["X",   "O",  "O" ],  # 0
            ["X",   "X",  None],  # 1
            [None, None,  "O" ],  # 2
        ]

        node = Node(board, "X")

        board_1 = copy.deepcopy(board)
        board_1[2][0] = "X"
        child_1 = Node(
            board=board_1,
            whos_turn_it_is="X"
        )

        board_2 = copy.deepcopy(board)
        board_2[2][1] = "X"
        child_2 = Node(
            board=board_2,
            whos_turn_it_is="X"
        )

        board_3 = copy.deepcopy(board)
        board_3[1][2] = "X"
        child_3 = Node(
            board=board_3,
            whos_turn_it_is="X"
        )

        children = node.next_stage()

        assert child_1 in children
        assert child_2 in children
        assert child_3 in children

        # we could do another example if we wanted

