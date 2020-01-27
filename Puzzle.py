import InputParser
import Board

inputPath = "input/input.txt"

def PrintAllAndInitialize(size, max_d, max_l, values): # To show all boards to search through
    board = []
    for i in range(len(size)):
        print()
        print("Puzzle #" + str(i) + " with max_d = " + str(max_d[i]) + " and max_l = " + str(max_l[i]) + ":")
        board.append(Board.Board(int(size[i]), values[i])) # Print every board
        print()
    return board

def SearchThroughInputs(size, board):
    for i in range(len(size)):
         movesList = board[i].GeneratePossibleMoves(int(size[i])) # We get n^2 possible moves every step
         print(movesList)

def main():
    # Initializing
    inputParser = InputParser.InputParser(inputPath)

    # Lists of all boards from the inputPath by column #
    size = inputParser.GetSizes()
    values = inputParser.GetValues()
    max_d = inputParser.GetMaxDepth()
    max_l = inputParser.GetMaxSearchPath()

    board = PrintAllAndInitialize(size, max_d, max_l, values) # Get a list of all the boards to search

    input("Run All Algorithms By Pressing Enter ")
    
    # Call algorithms here (take all boards in the input order)
    SearchThroughInputs(size, board)

main()