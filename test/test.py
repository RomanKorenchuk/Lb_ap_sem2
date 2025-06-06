import unittest
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, project_root)

from src.task import min_total_price
class TestMinTotalPrice(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(min_total_price([50, 20, 30, 17, 100], 10), "207.00")
        self.assertEqual(min_total_price([1, 2, 3, 4, 5, 6, 7], 100), "15.00")
        self.assertEqual(min_total_price([1, 1, 1], 33), "2.67")

unittest.main()