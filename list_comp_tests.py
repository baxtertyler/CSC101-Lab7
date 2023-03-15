# CPE 101-01
# LAB 7
# Name: Tyler Baxter
# Section: 03

# list comprehension tests
import unittest
from list_comp import *
from objects import *


class TestCases(unittest.TestCase):

    def test_point_distance_all(self):
        self.assertListEqual(point_distance_all([Point(3, 4), Point(5, 12), Point(6, 8)]), [5, 13, 10])
        self.assertListEqual(point_distance_all([Point(0, 0), Point(1, 1)]), [0, 1.4142135623730951])
        self.assertListEqual(point_distance_all([Point(10, 10), Point(5, 5)]), [14.142135623730951, 7.0710678118654755])

    def test_are_in_first_quadrant(self):
        self.assertListEqual(are_in_first_quadrant([Point(1, 1), Point(2, 2)]), [Point(1, 1), Point(2, 2)])
        self.assertListEqual(are_in_first_quadrant([Point(-1, -1), Point(-2, -2)]), [])
        self.assertListEqual(are_in_first_quadrant([Point(1, 1), Point(2, -2)]), [Point(1, 1)])

    def test_circle_distance_all(self):
        c1 = Circle(Point(3, 4), 1)
        c2 = Circle(Point(5, 12), 1)
        c3 = Circle(Point(6, 8), 1)
        c4 = Circle(Point(0, 10), 1)
        c5 = Circle(Point(10, 0), 1)
        self.assertListEqual(circle_distance_all([c1, c2]), [5, 13])
        self.assertListEqual(circle_distance_all([c3]), [10])
        self.assertListEqual(circle_distance_all([c4, c5]), [10, 10])

    def test_overlaps_all(self):
        c1 = Circle(Point(0, 0), 1)
        c2 = Circle(Point(3, 2), 7)
        c3 = Circle(Point(6, -2), 3)
        c4 = Circle(Point(-3, 8), 1)
        c5 = Circle(Point(4, 1), 10)
        self.assertListEqual(overlaps_all([c1, c2]), [c1, c2])
        self.assertListEqual(overlaps_all([c3, c5]), [c5])
        self.assertListEqual(overlaps_all([c4]), [])


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
