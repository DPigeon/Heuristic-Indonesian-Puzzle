import numpy as np

# Used to display the boards from the input

class Board:
    board = [] # The initial board list
    
    def __init__(self, n, values):  # Initialize
        self.ConstructBoard(n, values)
        self.DrawBoard(n)

    def ConstructBoard(self, n, values):
        self.board = np.zeros((n, n), dtype = int) # Initialize all with zeros
        individualValues = [int(x) for x in str(values)] # Converting the long integer to individual ints
        self.board = np.reshape(individualValues, (n, n)) # Converting from 1D array to 2D array

    def DrawBoard(self, n):
        print()
        for i in range(n):
            for j in range(n):
                print(self.board[i][j], end = "|")
            print()

    def GeneratePossibleMoves(self, n): # Generates all surrounding tiles of the possible touched tile
        # Inverse all possible move and store it in array of n^2. Then return it
        movesList = []
        for i in range(n):
            for j in range(n):
                if self.board[i][j] == 1:
                    movesList.append(self.ChangeSurroundings(self.board, i, j, 0, n))
                else:
                    movesList.append(self.ChangeSurroundings(self.board, i, j, 1, n))
        return movesList

    def ChangeSurroundings(self, board, i, j, tile, n):
        newBoard = board.copy()
        newBoard[i][j] = tile
        if i-1 >= 0:
            if newBoard[i-1][j] == 1:
                newBoard[i-1][j] = 0
            else:
                newBoard[i-1][j] = 1
        if i+1 < n:
            if newBoard[i+1][j] == 1:
                newBoard[i+1][j] = 0
            else:
                newBoard[i+1][j] = 1
        if j-1 >= 0:
            if newBoard[i][j-1] == 1:
                newBoard[i][j-1] = 0
            else:
                newBoard[i][j-1] = 1
        if j+1 < n:
            if newBoard[i][j+1] == 1:
                newBoard[i][j+1] = 0
            else:
                newBoard[i][j+1] = 1
        return newBoard