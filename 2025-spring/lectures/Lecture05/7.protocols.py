from typing import Any, Protocol, TypeVar
from collections.abc import Iterable

# The following code does not enforce type constraints on T correctly.

T = TypeVar("T")

def sort_items1(items: Iterable[T]) -> list[T]:
    return sorted(items)

lst = [object() for _ in range(4)]
sort_items1(lst)

# The following code enforces type constraints on T correctly by using a protocol.

class SupportsLessThan(Protocol):
    # For more information why positional-only arguments are used here, see https://github.com/microsoft/pyright/issues/5432#issuecomment-1622065339
    def __lt__(self, other: Any, /) -> bool:
        ...

LT = TypeVar("LT", bound=SupportsLessThan)

def sort_items2(items: Iterable[LT]) -> list[LT]:
    return sorted(items)

numbers = [5, 3, 8, 1, 9]
sort_items2(numbers)

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def __lt__(self, other: "Person") -> bool:
        return self.age < other.age  # Sorting by age
    
    def __repr__(self) -> str:
        return f"{self.name} ({self.age})"
    
people = [Person("Alice", 24), Person("Bob", 19), Person("Charlie", 30)]
sort_items2(people)


