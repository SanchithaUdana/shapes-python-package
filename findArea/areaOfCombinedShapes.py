from findArea import areaOfShapes as shape


def squareTriangle(squireLength, squireWidth, base, height):
    totalArea = (shape.square(squireLength, squireWidth) + shape.triangle(base, height))
    return totalArea


def rectangleTriangle(recLength, recWidth, triangleBase, triangleHeight):
    totalArea = (shape.rectangle(recLength, recWidth) + shape.triangle(triangleBase, triangleHeight))
    return totalArea


