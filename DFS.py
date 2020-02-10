import time
import Board
import Node
import OutputParser


class DFS:

    output_parser = OutputParser.OutputParser()
    timeStart = 0
    timeEnd = 0

    def __init__(self):
        self.open_list = []  # Nodes currently getting evaluated, as a stack
        self.closed_list = []  # List of nodes that has been visited
        self.open_dict = dict()
        self.closed_dict = dict()

        # Traversal search
    def DFS(self, iteration, board, size, max_depth):
        # Init files
        self.output_parser.init_search_files(iteration, "dfs")
        # Start timer
        self.timeStart = time.time()
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
                self.timeEnd = time.time()
                timeTaken = self.timeEnd - self.timeStart
                print('Time taken: ' + str(timeTaken) + ' second(s).\n')
                return True

            # If the current_node is at the max_depth and still hasn't found the goal state, don't generate children
            if current_node.get_depth() >= int(max_depth):
                continue

            # Put the current node in the closed list since it's been checked and not the goal state
            if current_node not in self.closed_dict:
                self.closed_dict[current_node] = 1
                self.closed_list.append(current_node)

            # Generate possible moves the board has, size^size is the number of the possible moves
            # Create nodes for each of the child nodes
            possible_moves = current_node.get_current_board().generate_possible_moves(int(size))
            for i in range(len(possible_moves)):
                children_to_append = Board.Board(int(size), current_node.get_current_board().prioritize_board(possible_moves)[i])
                node_to_add = Node.Node(current_node, children_to_append, current_node.get_depth()+1)
                current_node.add_children(node_to_add)

            # Generate a list of children to add by removing the one's already in the open and closed list
            children_to_add = [x for x in current_node.get_children() if x not in self.open_dict and self.closed_dict]

            for i in range(len(children_to_add)):
                self.open_dict[children_to_add[i]] = 1
            # Put remaining children to the front of the stack
            self.open_list[:0] = children_to_add
        print("Could not find a solution path for Puzzle #" + str(iteration) + "...\n")
        self.output_parser.create_solution_files(iteration, 'dfs', None, None, False)
        return False  # Open list is empty, and can't find a node at the goal state
