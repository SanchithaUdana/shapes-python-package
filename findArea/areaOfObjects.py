import math


def cube(length):
    area = (length * length) * 6
    print("Area of a cube : ", area, "square units")


def rectangular_prism(length, width, height):
    area = (2((width * length) + (height * length) + (height * width)))
    print("Area of a rectangular prism : ", area, "square units")


def Cylinder(radius, height):
    area = 2 * math.pi * radius(radius + height)
    print("Area of a cylinder : ", area, "square units")


def cone(radius, slant_height):
    area = math.pi * radius(radius + slant_height)
    print("Area of a cone : ", area, "square units")


def sphere(radius):
    area = 4 * math.pi * radius * radius
    print("Area of a sphere : ", area, "square units")


def hemisphere(radius):
    area = 3 * math.pi * radius * radius
    print("Area of a hemisphere : ", area, "square units")
