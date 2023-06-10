from findArea import areaOfObjects as object
from findArea import areaOfShapes as shape


def cubeHemisphere(length, radius):
    area = (object.cube(length) - shape.square(length)) + (object.hemisphere(radius) - shape.circle(radius))
    return area


def cubeSphere(length, radius):
    area = object.cube(radius) + object.cube(length)
    return area




