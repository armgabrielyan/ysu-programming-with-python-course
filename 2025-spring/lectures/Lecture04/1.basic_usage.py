def add_no_type(a, b):
    return a + b

# mypy with --disallow-incomplete-defs argument raises an error
def add_with_return_type(a, b) -> int:
    return a + b

def add_with_types(a: int, b: int) -> int:
    return a + b

# variables

x: int = 42
y: float = 4.2
text: str = "hello"
