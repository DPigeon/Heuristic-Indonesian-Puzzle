import InputParser
import Board

inputPath = "input/input.txt"

def PrintAll(size, max_d, max_l, values):
    for i in range(len(size)):
        print()
        print("Puzzle #" + str(i) + " with max_d = " + str(max_d[i]) + " max_l = " + str(max_l[i]))
        Board.Board(int(size[i]), int(values[i])) # Print every board

def main():
    # Initializing
    inputParser = InputParser.InputParser(inputPath)

    # Lists
    size = inputParser.GetSizes()
    values = inputParser.GetValues()
    max_d = inputParser.GetMaxDepth()
    max_l = inputParser.GetMaxSearchPath()
    
    PrintAll(size, max_d, max_l, values)

main()