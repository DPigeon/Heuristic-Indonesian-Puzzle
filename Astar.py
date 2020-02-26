import time
import heapq
import numpy as np
import Board
import Node
import OutputParser

# Priority Queue Sorted by h(n) --> BFS
# Priority Queue Sorted by f(n) --> A*

class Astar: # Using BFS in this class too as it is derived of A* with g = 0

    output_parser = OutputParser.OutputParser()
    timeStart = 0
    timeEnd = 0

    heuristic = None # The heuristic function
    # 0 --> counting heuristic
    # 1 --> future ahead 1 heuristic
    # 2 --> ???
    heuristicNum = 1 # Change this number to try different heuristics

    def __init__(self):
        self.open_list = [] # Nodes currently getting evaluated, as a priority queue
        self.closed_list = []  # List of nodes that has been visited
        heapq.heapify(self.open_list) # Using a priority queue as heap queue
        if self.heuristicNum == 0:
            self.heuristic = self.generate_heuristic_based_on_counting
        if self.heuristicNum == 1:
            self.heuristic = self.generate_heuristic_based_on_future_ones


    def Astar(self, iteration, board, size, max_length, name, stringName):
        length = 0
        # Init files
        self.output_parser.init_search_files(iteration, name)
        # Start timer
        self.timeStart = time.time()

        # Root node, which has a depth of 0
        fn = 0 + self.heuristic(board.board) # First f(n) has g = 0
        root_node = Node.Node(None, board, 0, fn)

        # Put the root node into the priority queue
        heapq.heappush(self.open_list, (root_node.f, root_node)) # Acts as pairs [<f(n), Node>]

        # While the open list has a node...
        while self.open_list:
            current_node = heapq.heappop(self.open_list) # We pop the smallest element to come according to f(n)
            f = current_node[0]
            g = 0 # For BFS
            if name == "astar":
                g = current_node[1].get_depth()
            h = self.heuristic(current_node[1].get_current_board().board)

            self.output_parser.create_search_files(iteration, name, f, g, h, current_node[1].get_current_board().transform_2d_to_1d())
            length = length + 1 # Increment the nodes searched

            # We look if the node is the state goal
            if current_node[1].get_current_board().check_goal_state():
                print("Found a solution path for Puzzle #" + str(iteration) + " with " + stringName + "!")
                self.closed_list.append(current_node[1])
                self.output_parser.create_solution_files(iteration, name, self.back_track(current_node[1]), True)
                self.timeEnd = time.time()
                timeTaken = self.timeEnd - self.timeStart
                print('Time taken: ' + str(timeTaken) + ' second(s).\n')
                return True

            # If the current_node is at the max_length and still hasn't found the goal state, don't generate children
            if length >= int(max_length):
                continue

            # Put the current node in the closed list since it's been checked and not the goal state
            if current_node[1] not in self.closed_list:
                self.closed_list.append(current_node[1])

            # Create nodes for each of the child nodes by generating the next moves
            possible_moves = current_node[1].get_current_board().generate_possible_moves(int(size))
            for i in range(len(possible_moves)):
                children_to_append = Board.Board(int(size), current_node[1].get_current_board().prioritize_board(possible_moves)[i])
                totalEstimate = self.heuristic(children_to_append.board) # For BFS
                if name == "astar":
                    totalEstimate = current_node[1].get_depth() + 1 + self.heuristic(children_to_append.board) # heuristic for A*
                node_to_add = Node.Node(current_node[1], children_to_append, current_node[1].get_depth() + 1, totalEstimate)
                current_node[1].add_children(node_to_add)

            # Generate a list of children to add by removing the one's already in the open and closed list
            children_to_add = [x for x in current_node[1].get_children() if x not in self.open_list and self.closed_list]

            # We add the next childrens to be checked with their estimate
            for i in range(len(children_to_add)):
                heapq.heappush(self.open_list, (children_to_add[i].get_estimate(), children_to_add[i]))

        print("Could not find a solution path for Puzzle #" + str(iteration) + " with " + stringName + ".\n")
        self.output_parser.create_solution_files(iteration, name, None, False)
        return False  # Open list is empty, and can't find a node at the goal state

    def generate_heuristic_based_on_counting(self, board):
        # Counting number of 1's and taking the smallest f priority for now as a heuristic for test
        h = np.count_nonzero(board)
        return h

    def generate_heuristic_based_on_future_ones(self, board):
        # Counts the number of 1's on the next move 1 step ahead and adds everything together
        total_number_of_ones = 0
        size = len(board)
        for i in range(size):
            for j in range(size):
                total_number_of_ones = total_number_of_ones + self.change_surroundings(board, i, j, size)

        return total_number_of_ones

    def change_surroundings(self, board, i, j, n):
        new_board = board.copy()  # Copy the list
        heuristic_to_return = 0
        # Change the current tile touched
        if new_board[i][j] == 1:
            heuristic_to_return += 1

        if i - 1 >= 0 and new_board[i - 1][j] == 1:  # left
            heuristic_to_return += 1
        if i + 1 < n and new_board[i + 1][j] == 1:  # right
            heuristic_to_return += 1
        if j - 1 >= 0 and new_board[i][j - 1] == 1:  # up
            heuristic_to_return += 1
        if j + 1 < n and new_board[i][j + 1] == 1:  # down
            heuristic_to_return += 1

        return heuristic_to_return

    def back_track(self, goal_node):
        back_track_list = []
        current_node = Node.Node(goal_node.get_parent(), goal_node.get_current_board(), goal_node.get_depth(), goal_node.get_estimate())
        back_track_list.append(current_node) # We add the goal state
        while current_node.get_parent() != None:
            back_track_list.insert(0, current_node.get_parent()) # We add each parents at the the beginning by back tracking
            current_node = current_node.get_parent() # We create the next one to iterate
        return back_track_list
