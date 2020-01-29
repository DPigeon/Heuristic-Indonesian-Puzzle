import Node

class DFS:

    def __init__(self):
        self.open_list = []     # Nodes currently getting evaluated, as a stack
        self.closed_list = []   # List of nodes that has been visited

    # Traversal search
    def DFS(self, root_node, goal_state):
        root_node = Node.Node(root_node)

        # Put the root node onto the stack
        self.open_list = [root_node]
        self.closed_list = []

        # While the open list has something
        while self.open_list:
            current_node = self.open_list.pop(0)   # Get the first element on the stack

            # If current node is the goal
            if current_node == goal_state:
                return True

            # Put the current node in the closed list since it's been checked and not the goal state
            if current_node not in self.closed_list:
                self.closed_list.append(current_node)

            # Generate a list of children to add by removing the one's already in the open nad closed list
            children_to_add = [x for x in current_node.get_children() if x not in self.open_list or self.closed_list]

            # Put remaining children to the stack
            self.open_list.append(children_to_add)

        return False    # Open list is empty, and can't find a node at the goal state



