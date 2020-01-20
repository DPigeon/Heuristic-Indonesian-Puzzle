import InputParser

inputPath = "input/input.txt"

def main():
	# 1. Program will take an input file .txt
	# 2. It will analyse with the DFS, BFS & A*
	# 3. It will output 6 files .txt
	
	input = InputParser.InputParser(inputPath)
	valueOfBoard1 = input.GetValues()
	print(valueOfBoard1[0]) # Shows the 0's and 1's we need for the board values

main()