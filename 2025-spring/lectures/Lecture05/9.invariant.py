from typing import TypeVar

def process_list(items: list[float]) -> None:
    print(items)

int_list = [1, 2, 3]
float_list = [1.1, 2.2, 3.3]

process_list(int_list)
process_list(float_list)

T = TypeVar("T") # Invariant by default
