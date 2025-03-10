from collections.abc import Iterable

def square_elements(it: Iterable[int]) -> list[int]:
    return [x ** 2 for x in it]


def gen():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

square_elements([1, 2, 3, 4, 5])
square_elements(range(1, 6))
square_elements(gen())
