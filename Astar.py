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

    def Astar(self, iteration, board, size, max_length):
        # Init files
        self.output_parser.init_search_files(iteration, "astar")
        # Start timer
        self.timeStart = time.time()
        # Root node, which has a depth of 0
        root_node = Node.Node(None, board, 0)

        # Evaluating f = g + h
        h = np.count_nonzero(root_node.get_current_board().board) # Counting number of 1's and taking the smallest f priority for now as a heuristic for test
        f = 0 + h

        # Put the root node onto the priority queue
        heapq.heappush(self.open_list, (f, root_node))
        self.closed_list = []

        # While the open list has something...
       
        print("Could not find a solution path for Puzzle #" + str(iteration) + ".\n")
        self.output_parser.create_solution_files(iteration, "astar", None, None, False)
        return False  # Open list is empty, and can't find a node at the goal state