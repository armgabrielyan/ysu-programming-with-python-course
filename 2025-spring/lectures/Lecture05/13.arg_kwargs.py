def sample_function(x: int, /, y: float, *args: str, **kwargs: bool) -> None:
    print(f"x: {x}, y: {y}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

sample_function(10, 2.5, "hello", "world", flag=True)
sample_function(10, 2.5, "hello", 17, flag=True)
sample_function(10, 2.5, "hello", "world", number=42)
