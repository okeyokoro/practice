from conway import transition

def test_board_1:
    board = [
        [1, 0, 1, 1, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [1, 1, 0, 0, 1]
    ]

    expected = [
        [1, 0, 1, 1, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [1, 1, 0, 0, 1]
    ]

    assert expected == transiton(board)


