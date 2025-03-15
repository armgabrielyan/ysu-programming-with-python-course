from typing import Callable, TypeVar

def process_number(func: Callable[[float], None]) -> None:
    func(42)

def print_int(n: int) -> None:
    print(f"Integer: {n}")

def print_float(n: float) -> None:
    print(f"Float: {n}")

def print_complex(n: complex) -> None:
    print(f"Complex: {n}")

process_number(print_int)
process_number(print_float)
process_number(print_complex)

T_contra = TypeVar("T_contra", contravariant=True)
