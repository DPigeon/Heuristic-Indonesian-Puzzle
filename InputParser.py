
class InputParser:
	size = [] # From 3 to 10
	max_depth_search = [] # For DFS
	max_search_path_length = [] # For BFS & A*
	values = [] # size^2 --> 9, 16, 25, 36, ... , 100
	
	def __init__(self, filePath): # Initialize
		with open(filePath) as file:
			for line in file:
				number = line.split() # Becoming strings. We have to convert to integer
				# Storing into separate lists
				self.size.append(number[0])
				self.max_depth_search.append(number[1])
				self.max_search_path_length.append(number[2])
				self.values.append(number[3])
	
	def get_sizes(self):
		return self.size
	
	def get_max_depth(self):
		return self.max_depth_search
		
	def get_max_search_path(self):
		return self.max_search_path_length
	
	def get_values(self):
		return self.values
