import copy
import Board


# A Node contains current info and is linked to other Node
class Node(object):

    def __init__(self, parent, board):
        self.parent = parent  # The parent node
        self.board = Board.Board(board)  # The current board configuration
        self.children = list()  # The nodes neighbour

    def __init__(self, node):
        self.copy_node = copy.deepcopy(node)    # Defines a copy constructor in order to call node

    def add_children(self, n):
        if n not in self.children:  # Making sure there are no duplicates
            self.children.append(n)

    def get_parent(self):
        return self.parent

    def get_current_board(self):
        return self.board

    def get_children(self):
        return self.children
