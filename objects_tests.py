# CPE 101-01
# LAB 7
# Name: Tyler Baxter
# Section: 03

import unittest
from objects import *


class TestCases(unittest.TestCase):

    def test_point(self):
        p1 = Point(0, 0)
        p2 = Point(3, 4)
        p3 = Point(3, 4)
        # __init__ tests
        self.assertEqual(p1.x, 0)
        self.assertEqual(p1.y, 0)
        self.assertEqual(p2.x, 3)
        self.assertEqual(p2.y, 4)
        # __eq__ tests
        self.assertEqual(p1 == p2, False)
        self.assertEqual(p3 == p2, True)
        # distance tests
        self.assertEqual(distance(p1, p2), 5)
        self.assertEqual(distance(p3, p2), 5)

    def test_circle(self):
        c1 = Circle(Point(0, 0), 1)
        c2 = Circle(Point(2, 4), 6)
        c3 = Circle(Point(2, 4), 6)
        # __init__ tests
        self.assertEqual(c1.center, Point(0, 0))
        self.assertEqual(c2.center, Point(2, 4))
        self.assertEqual(c1.rad, 1)
        self.assertEqual(c2.rad, 6)
        # __eg__ and __ne__ tests
        self.assertEqual(c1 == c2, False)
        self.assertEqual(c3 == c2, True)


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
