
class InputParser:
	size = [] # From 3 to 10
	maxDepthSearch = [] # For DFS
	maxSearchPathLength = [] # For BFS & A*
	values = [] # size^2 --> 9, 16, 25, 36, ... , 100
	
	def __init__(self, filePath): # Initialize
		with open(filePath) as file:
			for line in file:
				number = line.split()
				# Storing into separate lists
				self.size.append(number[0])
				self.maxDepthSearch.append(number[1])
				self.maxSearchPathLength.append(number[2])
				self.values.append(number[3])
	
	def GetSizes(self):
		return self.size
	
	def GetMaxDepth(self):
		return self.maxDepthSearch
		
	def GetMaxSearchPath(self):
		return self.maxSearchPathLength
	
	def GetValues(self):
		return self.values
