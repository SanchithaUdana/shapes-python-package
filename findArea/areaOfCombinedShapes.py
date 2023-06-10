from findArea import areaOfShapes as shape


def squareTriangle(squireLength, squireWidth, base, height):
    totalArea = (shape.square(squireLength, squireWidth) + shape.triangle(base, height))
    return totalArea


def rectangleTriangle(recLength, recWidth, triangleBase, triangleHeight):
    totalArea = (shape.rectangle(recLength, recWidth) + shape.triangle(triangleBase, triangleHeight))
    return totalArea


def hemiCircleSquire(radius, length):
    area = shape.hemiCircle(radius) + shape.square(length)
    return area


def rectangleTrapezium(length, width, length_of_parallel_sides, height):
    area = shape.rectangle(length, width) + shape.trapezium(length_of_parallel_sides, height)
    return area




