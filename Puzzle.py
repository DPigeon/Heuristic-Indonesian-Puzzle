import InputParser
import Board
import DFS

inputPath = "input/input.txt"


def print_all_and_initialize(size, max_d, max_l, values):  # To show all boards to search through
    board = []
    for i in range(len(size)):
        print()
        print("Puzzle #" + str(i) + " with max_d = " + str(max_d[i]) + " and max_l = " + str(max_l[i]) + ":")
        board.append(Board.Board(int(size[i]), values[i]))  # Print every board
        board[i].draw_board(int(size[i]))
        print()
    return board


def search_through_inputs(size, board):
    moves_list = []
    for i in range(len(size)):
        moves_list.append(board[i].generate_possible_moves(int(size[i])))  # We get n^2 possible move every step
    return moves_list


def main():
    # Initializing
    input_parser = InputParser.InputParser(inputPath)

    # Lists of all boards from the inputPath by column #
    size = input_parser.get_sizes()
    values = input_parser.get_values()
    max_d = input_parser.get_max_depth()
    max_l = input_parser.get_max_search_path()

    board = print_all_and_initialize(size, max_d, max_l, values)  # Get a list of all the boards to search

    input("Run All Algorithms By Pressing Enter ")


    # Call algorithms here (take all boards in the input order)
    for i in range(len(size)):
        # Now use those sorted boards with the DFS
        dfs_algorithm = DFS.DFS()
        dfs_algorithm.DFS(i, board[i], size[i], max_d[i])


main()
