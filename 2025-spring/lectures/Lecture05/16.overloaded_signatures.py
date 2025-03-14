from typing import overload

@overload
def process(data: int) -> str: ...
@overload
def process(data: list[int]) -> list[str]: ...
@overload
def process(data: dict[str, int]) -> dict[str, str]: ...

def process(data: int | list[int] | dict[str, int]) -> str | list[str] | dict[str, str]:
    if isinstance(data, int):
        return f"Processed integer: {data}"
    elif isinstance(data, list):
        return [f"Processed integer: {num}" for num in data]
    elif isinstance(data, dict):
        return {key: f"Processed integer: {value}" for key, value in data}
    else:
        raise TypeError("Unsupported type")

print(process(42))
print(process([1, 2, 3]))
print(process({"a": 10, "b": 20}))
print(process("hello"))  # Raises TypeError
