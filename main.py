# findArea is the package name
from findArea import areaOfShapes as shape
from findArea import areaOfObjects as object
from findArea import areaOfCombinedShapes as comShape
from findArea import areaOfCombinedObject as comObj

print(shape.circle(7))
print(object.Cylinder(7, 12))
print(comShape.squareTriangle(4, 5, 3))
print(comObj.cylinderCone(7, 8, 4))
