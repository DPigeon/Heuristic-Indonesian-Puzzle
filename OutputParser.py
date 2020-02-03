import os


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

        # How to use
        # outputParser = OutputParser.OutputParser()
        # outputParser.create_search_files(0, "dfs", 0, 0, 0, 101001101)

    def create_solution_files(self, iteration, algorithm, token, values, solution):
        parameters = ""

        if solution:
            parameters = token + " "
            for i in range(len(values)):
                parameters += str(values[i]) + " "
        else:
            parameters = "no solution"

        file = open("output/" + str(iteration) + "_" + algorithm + "_" + "solution.txt", "w")
        file.write(parameters)

        # How to use
        # outputParser = OutputParser.OutputParser()
        # outputParser.create_solution_files(0, "dfs", "0", 100101000, true)
