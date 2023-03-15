# CPE 101-01
# LAB 7
# Name: Tyler Baxter
# Section: 03

# unittest for objects
import unittest
from nested_list import *


class TestCases(unittest.TestCase):
    def test_groups_of_3(self):
        self.assertListEqual(group_of_3([1, 2, 3, 4, 5, 6]), [[1, 2, 3], [4, 5, 6]])
        self.assertListEqual(group_of_3([1, 2, 3, 4, 5]), [[1, 2, 3], [4, 5]])
        self.assertListEqual(group_of_3([1, 6, 3, 8, 3, 8, 2, 8, 2]), [[1, 6, 3], [8, 3, 8], [2, 8, 2]])
        self.assertListEqual(group_of_3([]), [])

    def test_final_value(self):
        self.assertListEqual(final_value([[1, 2], [3, 4], [5, 6]]), [2, 4, 6])
        self.assertListEqual(final_value([[1, 2, 3], [3, 4, 6], [7, 8, 9]]), [3, 6, 9])
        self.assertListEqual(final_value([[1, 6, 3, 7], [6, 9, 2], [], [1, 2]]), [7, 2, 2])
        self.assertListEqual(final_value([]), [])

    def test_repeat_value(self):
        self.assertListEqual(repeat_value([1, 2, 3]), [[1], [2, 2], [3, 3, 3]])
        self.assertListEqual(repeat_value([1, 5, 3, 0]), [[1], [5, 5, 5, 5, 5], [3, 3, 3], []])
        self.assertListEqual(repeat_value([8]), [[8, 8, 8, 8, 8, 8, 8, 8]])
        self.assertListEqual(repeat_value([]), [])


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
