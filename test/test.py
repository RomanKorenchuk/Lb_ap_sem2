import unittest
import math
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, project_root)

from src.mst import prim_mst

class TestPrimMST(unittest.TestCase):
    def test_triangle(self):
        graph = [
            [0, 1, 3],
            [1, 0, 2],
            [3, 2, 0]
        ]
        self.assertEqual(prim_mst(graph), 3)

    def test_disconnected(self):
        graph = [
            [0, math.inf, math.inf],
            [math.inf, 0, math.inf],
            [math.inf, math.inf, 0]
        ]
        self.assertEqual(prim_mst(graph), math.inf)

    def test_single_node(self):
        graph = [[0]]
        self.assertEqual(prim_mst(graph), 0)

if __name__ == "__main__":
    unittest.main()