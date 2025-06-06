import unittest
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, project_root)

from src.graph_root_finder import find_root_vertex

class TestGraphRootFinder(unittest.TestCase):
    def test_graph_with_single_root(self):
        graph = [
            [1, 2],
            [3],
            [],
            []
        ]
        n = 4
        self.assertEqual(find_root_vertex(graph, n), 0)

    def test_graph_with_multiple_roots(self):
        graph = [
            [1],
            [2],
            [0],
            [0, 1, 2]
        ]
        n = 4
        result = find_root_vertex(graph, n)
        self.assertIn(result, [3])

    def test_graph_without_root(self):
        graph = [
            [1],
            [],
            [3],
            []
        ]
        n = 4
        self.assertEqual(find_root_vertex(graph, n), -1)

    def test_single_vertex(self):
        graph = [[]]
        n = 1
        self.assertEqual(find_root_vertex(graph, n), 0)

    def test_disconnected_graph(self):
        graph = [
            [],
            [],
            []
        ]
        n = 3
        self.assertEqual(find_root_vertex(graph, n), -1)


if __name__ == "__main__":
    unittest.main()