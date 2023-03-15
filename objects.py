# CPE 101-01
# LAB 7
# Name: Tyler Baxter
# Section: 03

from utility import *
from math import fabs


class Point:
    # Representation of a point on a Cartesian plane with two attributes, x and y.
    def __init__(self, new_x: int, new_y: int):
        self.x = new_x
        self.y = new_y

    # Return True when both x and y attributes are equal and
    def __eq__(self, other) -> bool:
        return epsilon_equal(self.x, other.x) and epsilon_equal(self.y, other.y)

    # Return a string representing the point in the format "(x, y)".
    def __repr__(self) -> str:
        return "(" + str(self.x) + "," + str(self.y) + ")"


# Return the Euclidean distance between the calling Point and the argument Point.
def distance(self, to: Point) -> float:
    a = float(self.x - to.x)
    b = float(self.y - to.y)
    a_s = fabs(a ** 2)
    b_s = fabs(b ** 2)
    c_s = a_s + b_s
    c = float(c_s ** (1/2))
    return c


class Circle:
    # Representation of a circle using a Point as its center and a real number radius.
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.rad = radius

    # Return True when both center and radius attributes are equal and False otherwise.
    def __eq__(self, other) -> bool:
        return self.center == other.center and self.rad == other.rad

    # Return True when both center and radius attributes are not equal and False otherwise.
    def __ne__(self, other) -> bool:
        return not (self.center == other.center or self.rad == other.rad)

    # Return a string representing the circle in the format "#r @ (x, y)" where #r is the radius.
    def __repr__(self) -> str:
        return "#" + str(self.rad) + " @ (" + str(self.center.x) + ", " + str(self.center.y) + ")"


# Return True when the calling Circle overlaps with the argument Circle and False otherwise.
def overlaps(self, other: Circle) -> bool:
    return distance(self.center, other.center) < (self.rad + other.rad)
