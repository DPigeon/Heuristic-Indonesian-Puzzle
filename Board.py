import re
import copy

import numpy as np


# Used to display the boards from the input

class Board:
    board = []  # The initial board list

    def __init__(self, n, values):  # Initialize
        self.construct_board(n, values)

    def copy(self, board_to_copy):
        return copy.deepcopy(board_to_copy)

    def __hash__(self):
        return hash(str(self.board))

    def construct_board(self, n, values):
        self.board = np.zeros((n, n), dtype=int)  # Initialize all with zeros
        individual_values = [int(x) for x in str(values)]  # Converting the long integer to individual ints
        self.board = np.reshape(individual_values, (n, n))  # Converting from 1D array to 2D array

    def draw_board(self, n):
        print()
        for i in range(n):
            for j in range(n):
                print(self.board[i][j], end="|")
            print()

    def transform_2d_to_1d(self):
        result = ''
        for element in self.board.ravel():
            result += str(element)
        return result

    def neighbors(self, board, row, col):
        neighbor = [board[row][col]]

        if row - 1 >= 0:  # left
            neighbor.append(board[row - 1][col])
        if row + 1 < len(board[0]):  # right
            neighbor.append(board[row + 1][col])
        if col - 1 >= 0:  # up
            neighbor.append(board[row][col - 1])
        if col + 1 < len(board[0]):  # down
            neighbor.append(board[row][col + 1])

        if np.count_nonzero(neighbor) >= 3:
            return True
        else:
            return False

    def convert_position_to_tiles(self, row, column):

        # Char initilization, then transform to int
        char = 'A'
        row_start = ord(char[0])
        # Rows are defined by letters A...
        row_start += row
        return chr(row_start) + str(column + 1)

    def get_tiles_compare_boards(self, board):

        # Compare boards by returning a 2D array
        board_difference = np.subtract(self.board, board.board)

        # Store the index of values that are not 0
        for ix, iy in np.ndindex(board_difference.shape):
            if self.neighbors(board_difference, ix, iy):
                return self.convert_position_to_tiles(ix, iy)

    def generate_possible_moves(self, n):  # Generates all surrounding tiles of the possible touched tile
        # Inverse all possible move and store it in array of n^2. Then return it
        moves_list = []
        for i in range(n):
            for j in range(n):
                if self.board[i][j] == 1:
                    moves_list.append(self.change_surroundings(self.board, i, j, 0, n))  # Add all moves to an array
                else:
                    moves_list.append(self.change_surroundings(self.board, i, j, 1, n))
        return moves_list

    def change_surroundings(self, board, i, j, tile, n):
        new_board = board.copy()  # Copy the list
        new_board[i][j] = tile  # Change the current tile touched

        if i - 1 >= 0:  # left
            if new_board[i - 1][j] == 1:
                new_board[i - 1][j] = 0
            else:
                new_board[i - 1][j] = 1
        if i + 1 < n:  # right
            if new_board[i + 1][j] == 1:
                new_board[i + 1][j] = 0
            else:
                new_board[i + 1][j] = 1
        if j - 1 >= 0:  # up
            if new_board[i][j - 1] == 1:
                new_board[i][j - 1] = 0
            else:
                new_board[i][j - 1] = 1
        if j + 1 < n:  # down
            if new_board[i][j + 1] == 1:
                new_board[i][j + 1] = 0
            else:
                new_board[i][j + 1] = 1
        return new_board

    def prioritize_board(self, boards):
        # Sort the boards from higher to lower priority
        b = np.array(boards)
        size = len(b)
        flatten_boards = []
        values = []

        for i in range(size):  # We first, flatten the values in the list of boards then we join the values together
            # just like the input file. We then sort them
            flatten_boards.append(b[i].flatten())
            values.append(
                "".join(map(str, flatten_boards[i])))  # Convert the boards values into plain string to convert
        values.sort(key=self.natural_keys)  # Sort the values

        return values

    def check_goal_state(self):
        # Defining goal state
        row_count = self.board.shape[0]  # Getting the number of row/column
        goal_state = np.zeros((row_count, row_count), dtype=int)  # Defining our goal state which is a board of 0's
        return (goal_state == self.board).all()  # Checking if all elements are equal

    # for i in range(size)

    # Used to sort a string with integers inside (taken from human sorting
    # http://nedbatchelder.com/blog/200712/human_sorting.html)
    def atoi(self, text):
        return int(text) if text.isdigit() else text

    def natural_keys(self, text):
        return [self.atoi(c) for c in re.split(r'(\d+)', text)]
