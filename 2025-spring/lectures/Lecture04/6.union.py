from typing import Union

# def divide(x: Union[int, str], y: Union[int, str]) -> int:
def divide(x: int | str, y: int | str) -> int:
    return int(x) // int(y)

print(divide(10, 2))
print(divide("10", "2"))
print(divide(10, "2"))
print(divide("10", 2))
