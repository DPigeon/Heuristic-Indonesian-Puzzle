import InputParser
import Board

inputPath = "input/input.txt"

def main():
    # 1. Program will take an input file .txt
    # 2. It will analyse with the DFS, BFS & A*
    # 3. It will output 6 files .txt

    input = InputParser.InputParser(inputPath)
    size = int(input.GetSizes()[0])
    valueOfBoard1 = int(input.GetValues()[0])

    Board.Board(size, valueOfBoard1)

main()