import math


def cube(length):
    area = (length * length) * 6
    return area


def rectangular_prism(length, width, height):
    area = (2((width * length) + (height * length) + (height * width)))
    return area


def Cylinder(radius, height):
    area = 2 * math.pi * radius(radius + height)
    return area


def cone(radius, slant_height):
    area = math.pi * radius(radius + slant_height)
    return area


def sphere(radius):
    area = 4 * math.pi * radius * radius
    return area


def hemisphere(radius):
    area = 3 * math.pi * radius * radius
    return area
