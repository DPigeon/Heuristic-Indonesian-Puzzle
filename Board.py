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
        moveList = []
        for i in range(n):
            for j in range(n):
                leftX = i-1
                rightX = i+1
                upY = j-1
                downY = j+1
                if (leftX >= 0 or rightX < n) and (upY >= 0 or downY < n): # play with the conditions
                    if self.board[i][j] == 1:
                        self.board[i][j] = 0
                        moveList.append(self.board)
                    else:
                        self.board[i][j] = 1
                        moveList.append(self.board)
        print(moveList)
        return moveList