from typing import TypedDict

class Point2D(TypedDict):
    x: int
    y: int

point1 = Point2D(x=1, y=2)

print(point1)
print(type(point1))
print(point1["x"])
# print(point1.x) # Raises AttributeError because TypedDict does not support attribute access

point2: Point2D = {"x": 1, "y": 2}

point3 = Point2D(x=1, y="hello world") # No type checking at runtime

print(point3)
