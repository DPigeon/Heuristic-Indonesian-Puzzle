import os
import Board


class OutputParser:

    def __init__(self):
        super().__init__()

    def init_search_files(self, iteration, algorithm):
        file_name = "output/" + str(iteration) + "_" + algorithm + "_" + "search.txt"

        if os.path.exists(file_name):  # Delete it
            os.remove(file_name)
            file = open(file_name, "w")
            file.close()
        else:
            file = open(file_name, "w")
            file.close()

    def create_search_files(self, iteration, algorithm, f, g, h, values):
        if f < 1:
            f = 0
        if g < 1:
            g = 0
        if h < 1:
            h = 0

        file_name = "output/" + str(iteration) + "_" + algorithm + "_" + "search.txt"

        if os.path.exists(file_name):
            parameters = str(f) + " " + str(g) + " " + str(h) + " " + str(values) + "\n"
            file = open(file_name, "a")
            file.write(parameters)
            file.close()

    def create_solution_files(self, iteration, algorithm, values, solution):
        parameters = ""
        
        if solution:
            for i in range(len(values)):
                if values[i].get_parent() is not None:
                    parameters += str(values[i].get_parent().get_current_board().get_tiles_compare_boards(
                        values[i].get_current_board())) + " " + values[i].get_current_board().transform_2d_to_1d() + "\n"
                else:
                    parameters += "0" + " " + values[i].get_current_board().transform_2d_to_1d() + "\n"
        else:
            parameters = "no solution"

        file = open("output/" + str(iteration) + "_" + algorithm + "_" + "solution.txt", "w")

        file.write(parameters)
        file.close()

        count = 0
        file = "output/" + str(iteration) + "_" + algorithm + "_" + "solution.txt"
        with open(file, "r") as f:
            for line in f:
                count += 1
        print("Total number of moves is:", count - 1, "\n")
