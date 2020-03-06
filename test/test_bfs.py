import unittest
import sys
import os
sys.path.append('..')
import Astar
import Board

# Testing a 5x5 board (no solution) and a 3x3 board (solution)
# Test depends on the heuristic used

class BFSTest(unittest.TestCase):
    def test_bfs_1(self):
        pathOutput = "output/" # We create the output path for tests
        if not os.path.exists(pathOutput):
            os.makedirs(pathOutput)

        iteration = 0
        values = 1010101110000000000000000
        size = 5
        max_l = 9
        board = Board.Board(int(size), values)
        bfs_algorithm = Astar.Astar()
        self.assertEqual(bfs_algorithm.Astar(iteration, board, size, max_l, "bfs", "BFS"), True) # no solution
    
    def test_bfs_2(self):
        iteration = 1
        values = 111011011
        size = 3
        max_l = 10
        board = Board.Board(int(size), values)
        bfs_algorithm = Astar.Astar()
        self.assertEqual(bfs_algorithm.Astar(iteration, board, size, max_l, "bfs", "BFS"), True) # solution