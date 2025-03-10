from typing import Callable

def get_number() -> int:
    return 42

def get_float() -> float:
    return 3.14

def get_complex() -> complex:
    return 1 + 2j

def print_func_result(func: Callable[[], float]) -> None:
    print(func())

print_func_result(get_number)
print_func_result(get_float)
print_func_result(get_complex)
