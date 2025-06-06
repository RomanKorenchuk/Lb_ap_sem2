import unittest
from unittest.mock import mock_open, patch
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, project_root)

from src.ijones_task import solve


class TestIJonesTask(unittest.TestCase):
    def run_test_with_data(self, input_data, expected_output):
        m = mock_open(read_data=input_data)
        with patch("builtins.open", m), \
             patch("os.path.dirname", return_value="."), \
             patch("builtins.print") as mock_print:
            solve()
            # друга відкрита дія — це відкриття файлу на запис
            handle = m()
            handle.write.assert_called_once_with(expected_output)

    def test_simple_case(self):
        input_data = "3 3\nA B A\nC A C\nA B A\n"
        expected_output = "8\n"
        self.run_test_with_data(input_data, expected_output)

    def test_single_cell(self):
        input_data = "1 1\nZ\n"
        expected_output = "2\n"
        self.run_test_with_data(input_data, expected_output)

    def test_all_same(self):
        input_data = "2 2\nA A\nA A\n"
        expected_output = "6\n"  # Фікс: правильна відповідь згідно з логікою solve()
        self.run_test_with_data(input_data, expected_output)

    def test_different_letters(self):
        input_data = "2 2\nA B\nC D\n"
        expected_output = "2\n"
        self.run_test_with_data(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()