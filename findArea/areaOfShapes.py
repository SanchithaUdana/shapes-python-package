import math


def circle(radius):
    area = round((math.pi * radius * radius), 2)
    return area


def hemiCircle(radius):
    area = round(((math.pi * radius * radius)/2), 2)
    return area


def square(length):
    area = round((length * length))
    return area


def triangle(base, height):
    area = base * height * 0.5
    return area


def rectangle(length, width):
    area = length * width
    return area


def parallelogram(base, vertical_height):
    area = base * vertical_height
    return area


def trapezium(length_of_parallel_sides, height):
    area = length_of_parallel_sides * height * 0.5
    return area


def ellipse(a, b):
    area = math.pi * a * b
    return area


def kite(diagonal1, diagonal2):
    area = (diagonal1 * diagonal2) / 2
    return area


def rhombus(diagonal1, diagonal2):
    area = (diagonal1 * diagonal2) / 2
    return area


