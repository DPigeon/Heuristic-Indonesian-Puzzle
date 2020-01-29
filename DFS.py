
class DFS:

    def __init__(self):
        self.open_list = []     # Nodes currently getting evaluated, as a stack
        self.closed_list = []   # List of nodes that has been visited

    # Traversal search
    def DFS(self, root_node):

        # Put the root node onto the stack
        self.open_list = [root_node]
        self.closed_list = []

        # While the open list has something
        while self.open_list:
            current_node = self.open_list[0]    # Get the first element on the list

            # If current node is the goal

            # If 
            if current_node not in self.closed_list:
            #



