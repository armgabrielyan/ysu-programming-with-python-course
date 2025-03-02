from collections import deque
from collections.abc import Collection, Sequence

from typing import Any, List, Set


# def append_to_list(lst: List[int], item: int) -> None:
def append_to_list(lst: list[int], item: int) -> None:
    lst.append(item)

numbers = [1, 2, 3]
append_to_list(numbers, 4)
append_to_list(["a"], 4)

# def add_to_set(s: Set[int], item: int) -> None:
def add_to_set(s: set[int], item: int) -> None:
    s.add(item)

unique_numbers = {1, 2, 3}
add_to_set(unique_numbers, 4)


def rotate_deque(dq: deque[int], steps: int) -> None:
    dq.rotate(steps)

dq = deque([1, 2, 3, 4, 5])
rotate_deque(dq, 2)


# Collection is an abstract base class for all container types 
# that support size and membership operations.
def collection_length(coll: Collection[Any]) -> int:
    return len(coll)

coll1 = {1, 2, 3}
coll2 = [1, 2, 3]
collection_length(coll1)
collection_length(coll2)


# Sequence is an abstract base class for ordered collections (like lists and tuples) 
# that support indexing and slicing.
def first_element(seq: Sequence[int]) -> int:
    return seq[0]

seq = [10, 20, 30]
print(first_element(seq))
