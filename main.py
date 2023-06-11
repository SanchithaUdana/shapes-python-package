# findArea is the package name
from findArea import areaOfShapes as shape
from findArea import areaOfObjects as object
from findArea import areaOfCombinedShapes as comShape
from findArea import areaOfCombinedObject as comObj

print(round((shape.circle(7)), 2))
print(round((object.Cylinder(7, 12)), 2))
print(round((comShape.squareTriangle(4, 5, 3)), 2))
print(round((comObj.cylinderCone(7, 8, 4)), 2))
