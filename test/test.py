import unittest
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, project_root)

from src.task import BinaryTree, pre_order_traversal

class TestPreOrderTraversal(unittest.TestCase):

    def test_example_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.right = BinaryTree(5)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)
        self.assertEqual(pre_order_traversal(root), [1, 2, 5, 3, 6, 7])

if __name__ == '__main__':
    unittest.main()