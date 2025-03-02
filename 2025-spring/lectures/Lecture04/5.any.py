from typing import Any

def double1(x):
    return x * 2

def double2(x: Any) -> Any:
    return x * 2

print(double1(2))
print(double2(2))

print(double1("2"))
print(double2("2"))
