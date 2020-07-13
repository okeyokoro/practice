import random
import time
from copy import deepcopy
from pprint import pprint


board = [
    [0]*5,
    [0]*5,
    [0]*5,
    [0]*5,
    [0]*5,
]

def random_init(board):
    size = len(board)
    xboard = deepcopy(board)
    for i in range(size):
        for j in range(size):
            xboard[i][j] = random.choice([0, 1])

    return xboard

def get_live_neighbors(board, row, col):
    ans = 0
    for xrow, xcol in [( 1, -1), ( 1, 0), ( 1, 1),    # up row
                       ( 0, -1),          ( 0, 1),    # same row
                       (-1, -1), (-1, 0), (-1, 1),]:  # down row
        try:
            if board[row+xrow][col+xcol]:
                ans += 1
        except IndexError:
            pass
    return ans

def transition(board):
    size = len(board)
    xboard = deepcopy(board)

    for i in range(size):
        for j in range(size):
            element = board[i][j]
            live_neighbors = get_live_neighbors(board, i, j)

            if element and live_neighbors < 2:
                xboard[i][j] = 0
            elif element and live_neighbors > 3:
                xboard[i][j] = 0
            elif not element and live_neighbors == 3:
                xboard[i][j] = 1

    return xboard

def main(board):
    while True:
        pprint(board)
        print("=================")
        time.sleep(5)
        board = transition(board)


if __name__ == "__main__":
    board = random_init(board)
    main(board)

