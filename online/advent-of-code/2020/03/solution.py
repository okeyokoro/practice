
"""
    we know how many times we'll need to go down just by counting the number of rows in the input
    323
    we need the input width to be 323 * 3; since the slope is 3 right, 1 down

    for the final answer we dont count the first 3right we make.

    the only question is how do we repeat the pattern when we reach the limit of the right

    to expand it we need it to be 969 large; currently it is 24 characters large = 42
"""


def solution(lines, dcol, drow):
    maze = []
    for line in lines:
        maze.append([ i for i in line.strip()*200 ])

    # now the maze should be big enough
    row = 0
    col = 0
    ans = 0

    while row < len(maze):
        col += dcol
        row += drow

        try:
            if maze[row][col] == "#":
                ans += 1
        except:
            pass

    return ans


if __name__ == "__main__":
    print(
        solution(open("./input.txt"), dcol=1, drow=1)
        * solution(open("./input.txt"), dcol=5, drow=1)
        * solution(open("./input.txt"), dcol=7, drow=1)
        * solution(open("./input.txt"), dcol=1, drow=2)
        * 216
    )


