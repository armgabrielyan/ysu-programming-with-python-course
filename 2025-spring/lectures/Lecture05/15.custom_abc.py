from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class for different shapes."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Abstract property to get the name of the shape."""
        pass

    @abstractmethod
    def area(self) -> float:
        """Abstract method to calculate area."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Abstract method to calculate perimeter."""
        pass

    @classmethod
    @abstractmethod
    def from_dimensions(cls, *args) -> "Shape":
        """Abstract class method to create an instance from dimensions."""
        pass

    def describe(self) -> str:
        """Concrete method providing a general description."""
        return f"This is a {self.name} with an area of {self.area()} and a perimeter of {self.perimeter()}."

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height

    @property
    def name(self) -> str:
        return "Rectangle"

    def area(self) -> float:
        return self._width * self._height

    def perimeter(self) -> float:
        return 2 * (self._width + self._height)

    @classmethod
    def from_dimensions(cls, *args):
        """Class method to create a rectangle from dimensions."""
        width, height = args
        return cls(width, height)

class Circle(Shape):
    def __init__(self, radius: float):
        self._radius = radius

    @property
    def name(self) -> str:
        return "Circle"

    def area(self) -> float:
        return 3.14159 * self._radius ** 2

    def perimeter(self) -> float:
        return 2 * 3.14159 * self._radius

    @classmethod
    def from_dimensions(cls, *args):
        """Class method to create a circle from a radius."""
        radius = args[0]
        return cls(radius)

shapes = [
    Rectangle.from_dimensions(10, 5),
    Circle.from_dimensions(7)
]

for shape in shapes:
    print(shape.describe())

print(isinstance(Rectangle(1, 2), Shape))
print(isinstance(Circle(3), Shape))
print(issubclass(Rectangle, Shape))
print(issubclass(Circle, Shape))
