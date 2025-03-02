from typing import Tuple


# Tuple can be used as a record
def get_first_item(t: tuple[int, str, float]) -> int:
# def get_first_item(t: Tuple[int, str, float]) -> int:
    return t[0]

t = (10, "hello", 3.14)
get_first_item(t)

# Tuple can also be used as a variable-length sequence.
def compute_sum(t: tuple[int, ...]) -> int:
# def compute_sum(t: Tuple[int, ...]) -> int:
    return sum(t)

compute_sum((1, 2, 3))
compute_sum((1, 2, 3, 4, 5))
