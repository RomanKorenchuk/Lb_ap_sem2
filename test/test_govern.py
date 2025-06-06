import unittest

import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, project_root)

from src.govern import find_order

class TestGovern(unittest.TestCase):
    def test_simple_chain(self):
        input_data = [["b", "a"], ["c", "b"], ["d", "c"]]
        result = find_order(input_data)
        self.assertEqual(result, ["a", "b", "c", "d"])

    def test_multiple_dependencies(self):
        input_data = [["c", "a"], ["c", "b"]]
        result = find_order(input_data)
        self.assertTrue(result.index("a") < result.index("c"))
        self.assertTrue(result.index("b") < result.index("c"))

    def test_disconnected(self):
        input_data = [["b", "a"], ["d", "c"]]
        result = find_order(input_data)
        self.assertIn("a", result)
        self.assertIn("b", result)
        self.assertIn("c", result)
        self.assertIn("d", result)
        self.assertTrue(result.index("a") < result.index("b"))
        self.assertTrue(result.index("c") < result.index("d"))

if __name__ == "__main__":
    unittest.main()