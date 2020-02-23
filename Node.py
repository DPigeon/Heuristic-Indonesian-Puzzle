import copy


# A Node contains current info and is linked to other Node
class Node(object):

    def __init__(self, parent, board, depth, f):
        self.parent = parent  # The parent node
        self.board = board  # The current board configuration
        self.children = []  # The nodes neighbour
        self.depth = depth  # Get the node's current depth
        self.f = f # Estimate Heuristic f = g + h

    def __eq__(self, other):
        if type(other) is type(self):
            return (self.board.board == other.get_current_board().board).all()

    def __lt__(self, other): # Used in the priority queue
        if (self.f != None):
            return self.f < other.f

    def __hash__(self):
        return hash(str(self.board.board))

    def copy(self, node):
        return copy.deepcopy(node)  # Defines a copy constructor in order to call node

    def add_children(self, n):
        if n not in self.children:  # Making sure there are no duplicates
            self.children.append(n)

    def get_parent(self):
        return self.parent

    def get_current_board(self):
        return self.board

    def get_children(self):
        return self.children

    def get_depth(self):
        return self.depth
    
    def get_estimate(self):
        return self.f
