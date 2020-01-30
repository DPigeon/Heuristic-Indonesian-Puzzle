import numpy as np
import re
import copy

# Used to display the boards from the input

class Board:
    board = []  # The initial board list

    def __init__(self, n, values):  # Initialize
        self.ConstructBoard(n, values)
        self.DrawBoard(n)

    def copy(self, board_to_copy):
        return copy.deepcopy(board_to_copy)

    def ConstructBoard(self, n, values):
        self.board = np.zeros((n, n), dtype=int)  # Initialize all with zeros
        individualValues = [int(x) for x in str(values)]  # Converting the long integer to individual ints
        self.board = np.reshape(individualValues, (n, n))  # Converting from 1D array to 2D array

    def DrawBoard(self, n):
        print()
        for i in range(n):
            for j in range(n):
                print(self.board[i][j], end="|")
            print()

    def GeneratePossibleMoves(self, n):  # Generates all surrounding tiles of the possible touched tile
        # Inverse all possible move and store it in array of n^2. Then return it
        movesList = []
        for i in range(n):
            for j in range(n):
                if self.board[i][j] == 1:
                    movesList.append(self.ChangeSurroundings(self.board, i, j, 0, n))  # Add all moves to an array
                else:
                    movesList.append(self.ChangeSurroundings(self.board, i, j, 1, n))
        return movesList

    def ChangeSurroundings(self, board, i, j, tile, n):
        newBoard = board.copy()  # Copy the list
        newBoard[i][j] = tile  # Change the current tile touched

        if i - 1 >= 0:  # left
            if newBoard[i - 1][j] == 1:
                newBoard[i - 1][j] = 0
            else:
                newBoard[i - 1][j] = 1
        if i + 1 < n:  # right
            if newBoard[i + 1][j] == 1:
                newBoard[i + 1][j] = 0
            else:
                newBoard[i + 1][j] = 1
        if j - 1 >= 0:  # up
            if newBoard[i][j - 1] == 1:
                newBoard[i][j - 1] = 0
            else:
                newBoard[i][j - 1] = 1
        if j + 1 < n:  # down
            if newBoard[i][j + 1] == 1:
                newBoard[i][j + 1] = 0
            else:
                newBoard[i][j + 1] = 1
        return newBoard

    def PrioritizeBoard(self, boards):
        # Sort the boards from higher to lower priority
        b = np.array(boards)
        size = len(b)
        n = int(size ** 0.5)
        flattenBoards = []
        values = []
        individualValues = []
        sortedBoards = []

        for i in range(
                size):  # We first, flatten the values in the list of boards then we join the values together just like the input file. We then sort them
            flattenBoards.append(b[i].flatten())
            values.append("".join(map(str, flattenBoards[i])))  # Convert the boards values into plain string to convert
        values.sort(key=self.natural_keys)  # Sort the values

        for i in range(size):  # After sorted, we convert everything back to 2D arrays
            individualValues.append([int(x) for x in str(values[i])])  # Converting back to original 2D values
            sortedBoards.append(np.reshape(individualValues[i], (n, n)))  # Converting from 1D array to 2D array
        return sortedBoards

    def check_goal_state(self):
        # Defining goal state
        row_count = self.board.shape[0]                             # Getting the number of row/column
        goal_state = np.zeros((row_count, row_count), dtype=int)    # Defining our goal state which is a board of 0's
        return (goal_state == self.board).all()                     # Checking if all elements are equal

    # for i in range(size)

    # Used to sort a string with integers inside (taken from human sorting http://nedbatchelder.com/blog/200712/human_sorting.html)
    def atoi(self, text):
        return int(text) if text.isdigit() else text

    def natural_keys(self, text):
        return [self.atoi(c) for c in re.split(r'(\d+)', text)]
