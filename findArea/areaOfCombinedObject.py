import math
from findArea import areaOfObjects as object
from findArea import areaOfShapes as shape


def cubeHemisphere(length, radius):
    area = (object.cube(length) - shape.square(length)) + (object.hemisphere(radius) - shape.circle(radius))
    return area


def cubeSphere(length, radius):
    area = object.cube(radius) + object.cube(length)
    return area


def cylinderCone(radius, height, slant_height):
    total = object.Cylinder(radius, height) + object.cone(radius, slant_height)
    area = total - (2 * math.pi * radius * radius)
    return area






