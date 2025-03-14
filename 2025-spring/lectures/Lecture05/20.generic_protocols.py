from dataclasses import dataclass
import math
from typing import Protocol, SupportsAbs, runtime_checkable

def is_unit(value: SupportsAbs[float]) -> bool:
    return math.isclose(abs(value), 1.0)

@dataclass
class Vector:
    x: float
    y: float

    def __abs__(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)


print(is_unit(1))
print(is_unit(-1.0))
print(is_unit(0.5))
print(is_unit(Vector(0, 1)))
print(is_unit(Vector(1, 1)))


@runtime_checkable
class Closable(Protocol):
    def close(self): ...

print(isinstance(open("2025-spring/lectures/Lecture05/1.mapping.py"), Closable))
print(issubclass(type(open("2025-spring/lectures/Lecture05/1.mapping.py")), Closable))
