import math


def circle(radius):
    area = math.pi * radius * radius
    print("Area of a circle : ", area, "square units")


def square(length, width):
    area = length * width
    print("Area of a square : ", area, "square units")


def triangle(base, height):
    area = base * height * 0.5
    print("Area of a triangle : ", area, "square units")


def rectangle(length, width):
    area = length * width
    print("Area of a rectangle : ", area, "square units")


def parallelogram(base, vertical_height):
    area = base * vertical_height
    print("Area of a parallelogram : ", area, "square units")


def trapezium(length_of_parallel_sides, height):
    area = length_of_parallel_sides * height * 0.5
    print("Area of a trapezium : ", area, "square units")


def ellipse(a, b):
    area = math.pi * a * b
    print("Area of a ellipse : ", area, "square units")
