import InputParser
import Board
import Node
import collections

inputPath = "input/input.txt"


def PrintAllAndInitialize(size, max_d, max_l, values):  # To show all boards to search through
    board = []
    for i in range(len(size)):
        print()
        print("Puzzle #" + str(i) + " with max_d = " + str(max_d[i]) + " and max_l = " + str(max_l[i]) + ":")
        board.append(Board.Board(int(size[i]), values[i]))  # Print every board
        print()
    return board


def SearchThroughInputs(size, board):
    movesList = []
    for i in range(len(size)):
        movesList.append(board[i].GeneratePossibleMoves(int(size[i])))  # We get n^2 possible move every step
    return movesList


def build_tree(board, size, max_depth):
    # Root node
    node = Node.Node(None, board)
    queue = collections.deque([node])

    # Depending on the size of the queue and the dimensions of the the board,
    # We are able to build a tree according to the max depth -> queue size
    # should not be bigger than dimensions^max_depth

    while queue and len(queue) <= (int(size) * int(size)) ** int(max_depth):
        current_node = queue.popleft()
        # Generate possible move for that current node
        possible_moves = current_node.get_current_board().GeneratePossibleMoves(int(size))

        # Prioritize the board with all possible moves possible
        list_of_children = current_node.get_current_board().PrioritizeBoard(possible_moves)

        # Create nodes for each of the child nodes
        for i in range(len(list_of_children)):
            node_to_add = Node.Node(current_node, list_of_children[i])
            node.add_children(node_to_add)

        # Get back that list of children and add it to the queue
        queue += node.get_children()

    return node  # This is tree starting at the root


def main():
    # Initializing
    inputParser = InputParser.InputParser(inputPath)

    # Lists of all boards from the inputPath by column #
    size = inputParser.GetSizes()
    values = inputParser.GetValues()
    max_d = inputParser.GetMaxDepth()
    max_l = inputParser.GetMaxSearchPath()

    board = PrintAllAndInitialize(size, max_d, max_l, values)  # Get a list of all the boards to search

    input("Run All Algorithms By Pressing Enter ")

    build_tree(board[2], size[2], max_d[2])

    # Call algorithms here (take all boards in the input order)
    possibleMoves = SearchThroughInputs(size, board)  # Get a list of all possible moves
    for i in range(len(size)):
        print(board[i].PrioritizeBoard(possibleMoves[i]))  # Get the sorted by priority boards
        # Now use those sorted boards with the DFS


main()
