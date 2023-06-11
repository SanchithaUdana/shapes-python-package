import math
from findArea import areaOfShapes as shapes


def cube(length):
    area = (length * length) * 6
    return area


def rectangularPrism(length, width, height):
    area = (2 * ((width * length) + (height * length) + (height * width)))
    return area


def Cylinder(radius, height):
    area = (2 * math.pi * radius * height) + (2 * math.pi * radius * radius)
    return area


def cone(radius, slant_height):
    area = (math.pi * radius * (radius + slant_height))
    return area


def sphere(radius):
    area = 4 * math.pi * radius * radius
    return area


def hemisphere(radius):
    area = 3 * math.pi * radius * radius
    return area


def trianglePrism(base, height, length, width):
    area = (2 * shapes.triangle(base, height)) + (3 * shapes.rectangle(length, width))
    return area


def squareBasePyramid(baseLength, slantLength):
    area = round((baseLength * (baseLength + slantLength)))
    return area

