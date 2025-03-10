from collections.abc import Sequence
from random import shuffle
from typing import TypeVar

T = TypeVar("T")

def sample(population: Sequence[T], size: int) -> list[T]:
    if size < 1:
        raise ValueError("size must be >= 1")
    
    result = list(population)
    shuffle(result)

    return result[:size]

sample([1, 2, 3, 4, 5], 3)
sample("hello", 3)
