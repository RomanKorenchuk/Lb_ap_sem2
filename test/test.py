import unittest
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, project_root)

from src.list_based_priority_queue import PriorityQueue

class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.queue = PriorityQueue()

    def test_insert_and_peek(self):
        self.queue.insert("task1", 2)
        self.queue.insert("task2", 5)
        self.queue.insert("task3", 1)
        self.assertEqual(self.queue.peek(), "task2")
        print(self.queue)

    def test_pop(self):
        self.queue.insert("task1", 3)
        self.queue.insert("task2", 4)
        self.queue.insert("task3", 2)
        self.assertEqual(self.queue.pop(), "task2")
        self.assertEqual(self.queue.pop(), "task1")
        self.assertEqual(self.queue.pop(), "task3")
        self.assertIsNone(self.queue.pop())

    def test_equal_priority(self):
        self.queue.insert("task1", 5)
        self.queue.insert("task2", 5)
        self.queue.insert("task3", 5)
        self.assertEqual(self.queue.pop(), "task1")
        self.assertEqual(self.queue.pop(), "task2")
        self.assertEqual(self.queue.pop(), "task3")

if __name__ == '__main__':
    unittest.main()
