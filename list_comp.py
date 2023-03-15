# CPE 101-01
# LAB 7
# Name: Tyler Baxter
# Section: 03

from objects import *


# Computes and returns a list containing the distance from the origin (0, 0)
# to the corresponding point in the input list.
def point_distance_all(points: list[Point]) -> list[float]:
    return [distance(p, Point(0, 0)) for p in points]


# Returns all points in the input list that are in the first quadrant.
def are_in_first_quadrant(points: list[Point]) -> list[Point]:
    return [p for p in points if p.x > 0 and p.y > 0]


# Return a list containing the distance from the origin (0, 0)
# to the corresponding circle in the input list.
def circle_distance_all(circles: list[Circle]) -> list[float]:
    return [distance(c.center, Point(0, 0)) for c in circles]


# Return a list of a Circle objects in the given list that overlap with the unit circle.
def overlaps_all(circles: list[Circle]) -> list[Circle]:
    return [c for c in circles if overlaps(c, Circle(Point(0, 0), 1))]
