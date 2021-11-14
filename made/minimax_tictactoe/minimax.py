"""
An unbeatable CLI TicTacToe game
"""

import copy
import collections
from pandas import DataFrame

board = [
    [None, None, None],
    [None, None, None],
    [None, None, None],
]


options = ("X", "O")

the_human_is = 0 # convenient default


def let_the_human_choose_a_letter():
    print("""
    Pick the letter you want to play as!

    Options:
    - X (you play first)
    - O (you play second)

    """)

    not_answered = True
    letter = None

    while not_answered:

        letter = input(">>>")

        if letter.lower() == "x":
            the_human_is = 0
            not_answered = False
        elif letter.lower() == "o":
            the_human_is = 1
            not_answered = False
        else:
            print("""
            You messed that up...
            ...Sigh...
            Try again

            """)

    return letter


class Board():
    def __init__(self, board):
        self.board = board

    @property
    def is_terminal(self):
        return self.who_won(self.board)

    @classmethod
    def who_won(cls, board):
        """
            - test the board for a `winning_constellation`
                - ^ I probably need to have the CO-ORDINATES
                - ^ which would make it easier to check
            - return the letter of the player that won
        """

        # first-element:  row
        # second-element: col
        winning_coordinates = (
            # Vertical
            [ (0,1), (1,1), (2,1) ], # all of the middle column
            [ (0,0), (1,0), (2,0) ], # all of the first column
            [ (0,2), (1,2), (2,2) ], # all of the last column

            # Horizontal
            [ (0,0), (0,1), (0,2) ], # all of the first row
            [ (1,0), (1,1), (1,2) ], # all of the second row
            [ (2,0), (2,1), (2,2) ], # all of the last row

            # Diagonal
            [ (0,0), (1,1), (2,2) ],
            [ (2,0), (1,1), (0,2) ],
        )

        for co in winning_coordinates:
            one_row, one_col  = co[0]
            two_row, two_col = co[1]
            three_row, three_col = co[2]

            if board[one_row][one_col] == board[two_row][two_col] == board[three_row][three_col]:
                return board[one_row][one_col]

        return None

    @classmethod
    def get_empty_spaces(cls, board):
        ans = []

        for row in range(3):
            for col in range(3):
                if board[row][col] == None:
                    ans.append( (row, col) )

        return ans


class Node():
    """ A Node in the MiniMax Tree """

    # we maximize / minimize from the perspective of the AI
    the_AI_is = None

    def __init__(self, board, whos_turn_it_is, parent=None):
        self.board = board # TODO: perhaps use `Board` class instead
        self.whos_turn_it_is = whos_turn_it_is

        self.parent = parent
        if not parent:
            Node.the_AI_is = whos_turn_it_is

        # has to be computed
        self.score = None
        self.children = []

    def __str__(self):
        return (
            "===== Node ====="
            f"\n{DataFrame(self.board).to_string(index=False, header=False)}\n"
            "===== Node =====\n"
        )

    def __eq__(self, node):
        """ Needed to do this for `assert`s to work """
        return node.board == self.board

    def score_this_leaf_node(self, who_won=None):
        """ """
        no_winner = who_won == None
        if no_winner:
            self.score = 0
        elif who_won == Node.the_AI_is:
            self.score = 1
        elif who_won == Node.alternate_turns(Node.the_AI_is):
            self.score = -1

        print(f"We scored a Node!\nScore: {self.score}")
        return self.score

    def next_stage(self):
        """ Create children! """
        # TODO: use `Board()`. do `self.board.is_terminal`

        someone_won = Board.who_won(self.board)
        if someone_won:
            print(f"There is no next stage\n{someone_won} won!")
            self.score_this_leaf_node(someone_won)
            return None

        available_positions = Board.get_empty_spaces(self.board)
        if not available_positions:
            print("There is no next stage\nIt was a tie!")
            self.score_this_leaf_node()
            return None

        for pos in available_positions:
            row, col = pos
            new_board = copy.deepcopy(self.board)
            new_board[row][col] = self.whos_turn_it_is

            new_node = Node(
                board=new_board,
                whos_turn_it_is=Node.alternate_turns(self.whos_turn_it_is),
                parent=self,
            )

            print(new_node)

            self.children.append(new_node)

        return self.children

    @classmethod
    def alternate_turns(cls, letter):
        if letter.lower() == "x":
            return "O"
        elif letter.lower() == "o":
            return "X"


class MiniMax():
    """
        - Take in a board at a particular stage in the game

        - Make the Tree of all the possible moves
            - ^ iterate through empty spaces on the board; create children Nodes
                - ^ the process is recursive

        - Do a Search on the Tree
            - ^ "bubble up" the scores on the nodes
    """
    def __init__(self, root:Node):
        self.root = root
        self.non_leaf_nodes = collections.deque([])

    def generate_tree_from_root(self, depth=float("inf")):

        q = collections.deque([self.root])

        while q:
            n = q.popleft()

            n_children = n.next_stage()

            if n_children:
                self.non_leaf_nodes.append(n)

                for child in n_children:
                    # TODO: put the leaf nodes in q first
                    #       ^ we can sort by checking if the node has a score
                    #
                    # TODO: we can stop the iteration if we've found a Node with score == 1
                    q.append(child)

        print("Generated all of the Tree!\n")

    def bubble_up_scores_with_min_max(self):
        while self.non_leaf_nodes:
            scores = []

            n = self.non_leaf_nodes.pop()

            for c in n.children:
                scores.append(c.score)

            scores = sorted(scores)

            if n.whos_turn_it_is != Node.the_AI_is:
                # we minimize
                # i.e. choose the lowest number
                n.score = scores[0]
            else:
                # we maximize
                # i.e. chose the largest number
                n.score = scores[-1]

            print(f"We gave the Node a score of: {n.score}")
            print(f"These are it's children's scores: {scores}")
            print(n)

    def best_move(self):
        """
            Do a BFS to render the best immediate move

            We do this by searching children
            until we find a leaf node with a positive score
            ( or more robustly; the leaf node with the most positive score )

            Once we find the leaf node;
            We bubble up, until we find the parent closest to the root
        """
        q = collections.deque([self.root])

        best_leaf = None

        while not best_leaf:
            n = q.popleft()

            # HACK: we need to accomodate ties too
            if n.score == 1 and not n.children:
                # Winning Score & No Children (i.e Leaf Node)
                print("We've found a winning path")
                print(n)
                best_leaf = n

            for child in n.children:
                q.append(child)

        nearest_node_on_the_best_path = None

        while not nearest_node_on_the_best_path:
            if best_leaf.parent == self.root:
                # we've reached the nearest_node_on_the_best_path
                nearest_node_on_the_best_path = best_leaf

            best_leaf = best_leaf.parent

        print("Best Move:")
        print(nearest_node_on_the_best_path)
        return nearest_node_on_the_best_path



