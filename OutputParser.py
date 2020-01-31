
class OutputParser:
    
    def __init__(self):
        super().__init__()
    
    def create_search_files(self, iteration, algorithm, f, g, h, values):
        if f < 1:
            f = 0
        if g < 1:
            g = 0
        if h < 1:
            h = 0

        parameters = str(f) + " " + str(g) + " " + str(h) + " " + str(values) + "\n"
        file = open("output/" + str(iteration) + "_" + algorithm + "_" + "search.txt", "w")
        file.write(parameters)

        #outputParser = OutputParser.OutputParser()
        #outputParser.create_search_files(0, "dfs", 0, 0, 0, 101001101)
