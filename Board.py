import numpy as np

# Used to display the boards from the input

class Board:
    board = [] # The board list
    
    def __init__(self, n, values):  # Initialize
        self.ConstructBoard(n, values)

        print()
        print("Puzzle #1")
        print()
        for i in range(n):
            for j in range(n):
                print(self.board[i][j], end = "|")
            print()

    def ConstructBoard(self, n, values):
        self.board = np.zeros((n, n), dtype = int) # Initialize all with zeros
        individualValues = [int(x) for x in str(values)] # Converting the long integer to individual ints
        self.board = np.reshape(individualValues, (n, n)) # Converting from 1D array to 2D array


