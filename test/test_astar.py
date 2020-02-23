import unittest
import sys
import os
sys.path.append('..')
import Astar
import Board

# Testing a 3x3 board (no solution) and a 5x5 board (solution)

class AstarTest(unittest.TestCase):
    def test_astar_1(self):
        pathOutput = "output/" # We create the output path for tests
        if not os.path.exists(pathOutput):
            os.makedirs(pathOutput)

        iteration = 0
        values = 111111111
        size = 3
        max_l = 10
        board = Board.Board(int(size), values)
        astar_algorithm = Astar.Astar()
        self.assertEqual(astar_algorithm.Astar(iteration, board, size, max_l), False) # no solution
    
    def test_astar_2(self):
        iteration = 1
        values = 1010101110000000000000000
        size = 5
        max_l = 9
        board = Board.Board(int(size), values)
        astar_algorithm = Astar.Astar()
        self.assertEqual(astar_algorithm.Astar(iteration, board, size, max_l), True)