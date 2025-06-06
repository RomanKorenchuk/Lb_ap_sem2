import unittest
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, project_root)

from src.task import is_subarray
 
class TestIsSubarray(unittest.TestCase):
    def test_cases(self):
        self.assertTrue(is_subarray([1,2,3], [1,2,3,4]))
        self.assertFalse(is_subarray([4,2], [1,2,3,4]))
        self.assertTrue(is_subarray([1,3,5], [1,2,3,4,5]))
        self.assertTrue(is_subarray([], [1,2,3]))
        self.assertFalse(is_subarray([1,2,3], []))
        self.assertTrue(is_subarray([4,2,3], [0,4,2,3,1]))

unittest.main()