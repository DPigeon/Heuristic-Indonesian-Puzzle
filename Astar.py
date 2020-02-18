import time
import heapq
import numpy as np
import Board
import Node
import OutputParser


class Astar:

    output_parser = OutputParser.OutputParser()
    timeStart = 0
    timeEnd = 0

    def __init__(self):
        self.open_list = [] # Nodes currently getting evaluated, as a priority queue
        self.closed_list = []  # List of nodes that has been visited
        heapq.heapify(self.open_list) # Using a priority queue as heap queue
        heapq.heapify(self.closed_list)

    def evaluate_heuristic_1(self, board):
        # Counting number of 1's and taking the smallest f priority for now as a heuristic for test
        h = np.count_nonzero(board)
        return h

    def Astar(self, iteration, board, size, max_length):
        length = 0
        # Init files
        self.output_parser.init_search_files(iteration, "astar")
        # Start timer
        self.timeStart = time.time()
        # Root node, which has a depth of 0
        root_node = Node.Node(None, board, 0)
        
        fn = 0 + self.evaluate_heuristic_1(root_node.get_current_board().board) # First f(n) has g = 0

        # Put the root node into the priority queue
        heapq.heappush(self.open_list, (fn, root_node)) # Acts as pairs [<f(n), Node>]

        # While the open list has a node...
        while self.open_list:
            current_node = heapq.heappop(self.open_list) # We pop the smallest element to come according to f(n)
            f = current_node[0]
            g = current_node[1].get_depth()
            h = self.evaluate_heuristic_1(current_node[1].get_current_board().board)

            self.output_parser.create_search_files(iteration, "astar", f, g, h, current_node[1].get_current_board().transform_2d_to_1d())
            length = length + 1 # Increment the nodes searched
       
            # We look if the node is the state goal
            if current_node[1].get_current_board().check_goal_state():
                print("Found a solution path for Puzzle #" + str(iteration) + "!")
                self.closed_list.append(current_node[1])
                self.output_parser.create_solution_files(iteration, "astar", 'None', self.closed_list, True)
                self.timeEnd = time.time()
                timeTaken = self.timeEnd - self.timeStart
                print('Time taken: ' + str(timeTaken) + ' second(s).\n')
                return True

            # If the current_node is at the max_length and still hasn't found the goal state, don't generate children
            if length >= int(max_length):
                continue
            
            # Put the current node in the closed list since it's been checked and not the goal state
            if current_node not in self.closed_list: 
                heapq.heappush(self.closed_list, (f, current_node[1]))

            # Create nodes for each of the child nodes by generating the next moves
            possible_moves = current_node[1].get_current_board().generate_possible_moves(int(size))
            for i in range(len(possible_moves)):
                children_to_append = Board.Board(int(size), current_node[1].get_current_board().prioritize_board(possible_moves)[i])
                node_to_add = Node.Node(current_node[1], children_to_append, current_node[1].get_depth() + 1)
                current_node[1].add_children(node_to_add)

            # Generate a list of children to add by removing the one's already in the open and closed list
            children_to_add = [x for x in current_node[1].get_children() if x not in self.open_list and self.closed_list]

            print(children_to_add)
            # We add the next childrens to be checked with their estimate
            for i in range(len(children_to_add)):
                totalEstimate = children_to_add[i].get_depth() + self.evaluate_heuristic_1(children_to_add[i].get_current_board().board) # heuristic
                heapq.heappush(self.open_list, (totalEstimate, children_to_add[i]))

        print("Could not find a solution path for Puzzle #" + str(iteration) + ".\n")
        self.output_parser.create_solution_files(iteration, "astar", None, None, False)
        return False  # Open list is empty, and can't find a node at the goal state