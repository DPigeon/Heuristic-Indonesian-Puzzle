import InputParser
import Board

inputPath = "input/input.txt"

def main():
    # 1. Program will take an input file .txt
    # 2. It will analyse with the DFS, BFS & A*
    # 3. It will output 6 files .txt

    inputParser = InputParser.InputParser(inputPath)
    size = inputParser.GetSizes()
    for i in range(len(size)):
        size = int(inputParser.GetSizes()[i])
        valueOfBoard1 = int(inputParser.GetValues()[i])
        Board.Board(size, valueOfBoard1) # Print every board

main()