import Node
import Board
import OutputParser


class DFS:

    output_parser = OutputParser.OutputParser()

    def __init__(self):
        self.open_list = []  # Nodes currently getting evaluated, as a stack
        self.closed_list = []  # List of nodes that has been visited

    # Traversal search
    def DFS(self, iteration, board, size, max_depth):
        # Init files
        self.output_parser.init_search_files(iteration, "dfs")
        # Root node, which has a depth of 0
        root_node = Node.Node(None, board, 0)

        # Put the root node onto the stack
        self.open_list = [root_node]
        self.closed_list = []

        # While the open list has something
        while self.open_list:
            current_node = self.open_list.pop(0)  # Get the first element on the stack
            self.output_parser.create_search_files(iteration, "dfs", 0, 0, 0, current_node.get_current_board().transform_2d_to_1d())

            # If current node is the goal
            if current_node.get_current_board().check_goal_state():
                print("Found a solution path for Puzzle #" + str(iteration) + "!")
                self.closed_list.append(current_node)
                self.output_parser.create_solution_files(iteration, 'dfs', 'None', self.closed_list, True)
                return True

            # If the current_node is at the max_depth and still hasn't found the goal state, don't generate children
            if current_node.get_depth() >= int(max_depth):
                continue

            # Put the current node in the closed list since it's been checked and not the goal state
            if current_node not in self.closed_list:
                self.closed_list.append(current_node)

            # Generate possible moves the board has, size^size is the number of the possible moves
            possible_moves = current_node.get_current_board().generate_possible_moves(int(size))
            list_of_children = []
            for i in range(len(possible_moves)):
                children_to_append = Board.Board(int(size), current_node.get_current_board().prioritize_board(possible_moves)[i])
                list_of_children.append(children_to_append)

            # Create nodes for each of the child nodes
            for i in range(len(list_of_children)):
                node_to_add = Node.Node(current_node, list_of_children[i], current_node.get_depth()+1)
                current_node.add_children(node_to_add)

            # Generate a list of children to add by removing the one's already in the open nad closed list
            children_to_add = [x for x in current_node.get_children() if x not in self.open_list or self.closed_list]

            # Put remaining children to the front of the stack
            self.open_list[:0] = children_to_add
        print("Could not find a solution path for Puzzle #" + str(iteration) + "...")
        self.output_parser.create_solution_files(iteration, 'dfs', None, None, False)
        return False  # Open list is empty, and can't find a node at the goal state
