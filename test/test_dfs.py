import unittest
import sys
import os
sys.path.append('..')
import DFS
import Board

# Testing a 4x4 board (solution) and a 3x3 board (no solution)

class DfsTest(unittest.TestCase):
    def test_dfs_1(self):
        pathOutput = "output/" # We create the output path for tests
        if not os.path.exists(pathOutput):
            os.makedirs(pathOutput)

        iteration = 0
        values = 1010010111001010
        size = 4
        max_d = 15
        board = Board.Board(int(size), values)
        dfs_algorithm = DFS.DFS()
        self.assertEqual(dfs_algorithm.DFS(iteration, board, size, max_d), True)
    
    def test_dfs_2(self):
        iteration = 1
        values = 111001011
        size = 3
        max_d = 2
        board = Board.Board(int(size), values)
        dfs_algorithm = DFS.DFS()
        self.assertEqual(dfs_algorithm.DFS(iteration, board, size, max_d), False)