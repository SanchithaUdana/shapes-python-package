# findArea is the package name
from findArea import areaOfShapes as shape
from findArea import areaOfObjects as object
from findArea import areaOfCombinedShapes as comShape
from findArea import areaOfCombinedObject as comObj

print("Area of circle : ", round((shape.circle(7)), 2), "squire unit")
print("Area of cylinder :  ", round((object.Cylinder(7, 12)), 2), "squire unit")
print("Area of Square Triangle :  ", round((comShape.squareTriangle(4, 5, 3)), 2), "squire unit")
print("Area of Cylinder Cone : ", round((comObj.cylinderCone(7, 8, 4)), 2), "squire unit")

# Example Function Calling using findArea package
shape.square(2)
object.cone(7, 12)
comShape.hemiCircleSquire(7, 12)
comObj.cubeHemisphere(12, 7)
# we can call all of functions using own object name



