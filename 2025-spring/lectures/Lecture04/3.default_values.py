from typing import Optional, Union

def greet(name: str = "Guest") -> str:
    return f"Hello, {name}!"

print(greet())
print(greet("Alice"))

def greet_with_optional(name: Optional[str] = None) -> str:
# def greet_with_optional(name: str | None = None) -> str:
    if name is None:
        return "Hello, Guest!"
    return f"Hello, {name}!"

print(greet_with_optional())
print(greet_with_optional("Alice"))

