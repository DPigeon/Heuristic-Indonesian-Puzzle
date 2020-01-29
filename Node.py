# A Node contains current info and is linked to other Node
class Node(object):

    def __init__(self, parent, board):
        self.parent = parent    # The parent node
        self.board = board      # The current configuration
        self.children = list()  # The nodes neighbour

    def add_children(self, n):
        if n not in set(self.children):
            self.children.extend(n)
