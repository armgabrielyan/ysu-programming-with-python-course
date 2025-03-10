from typing import Any, Callable

def apply_function(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

def add(x: int = 4, y: int = 2) -> int:
    return x + y

def greet(name: str = "world") -> str:
    return f"Hello, {name}!"

apply_function(add, 2, 3)
apply_function(greet, 2, 3)

def log_function(func: Callable[..., Any]) -> None:
    print(func())

log_function(add)
log_function(greet)

