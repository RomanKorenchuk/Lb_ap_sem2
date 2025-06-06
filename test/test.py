import unittest
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, project_root)

from src.task import rabin_karp_search

class TestRabinKarp(unittest.TestCase):
    def test_basic_match(self):
        self.assertEqual(rabin_karp_search("абракадабраабракадабраабракадабра", "кадабра"), [4, 15, 26])

    def test_no_match(self):
        self.assertEqual(rabin_karp_search("abracadabra", "xyz"), [])

    def test_empty_needle(self):
        self.assertEqual(rabin_karp_search("abracadabra", ""), [])

    def test_empty_haystack(self):
        self.assertEqual(rabin_karp_search("", "abra"), [])

    def test_full_match(self):
        self.assertEqual(rabin_karp_search("abc", "abc"), [0])

    def test_overlap(self):
        self.assertEqual(rabin_karp_search("aaaaa", "aa"), [0, 1, 2, 3])

if __name__ == "__main__":
    unittest.main()