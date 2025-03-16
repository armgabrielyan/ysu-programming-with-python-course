from typing import TypeVar, Generic

T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        if not self._items:
            raise IndexError("Pop from empty stack")
        return self._items.pop()

    def peek(self) -> T:
        if not self._items:
            raise IndexError("Peek from empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        return not self._items

# Stack for integers
int_stack = Stack[int]()
int_stack.push(10)
int_stack.push(20)

print(int_stack.pop())
print(int_stack.peek())

int_stack.push("hello")

# Stack for strings
str_stack = Stack[str]()
str_stack.push("hello")
str_stack.push("world")

print(str_stack.pop())
print(str_stack.peek())

str_stack.push(42)


# Generic Class with Multiple Type Variables

K = TypeVar("K") # Type for cache keys
V = TypeVar("V") # Type for cache values

class Cache(Generic[K, V]):
    def __init__(self) -> None:
        self._storage: dict[K, V] = {}

    def set(self, key: K, value: V) -> None:
        """Store a value in the cache."""
        self._storage[key] = value

    def get(self, key: K) -> V | None:
        """Retrieve a value from the cache (or None if not found)."""
        return self._storage.get(key)

    def remove(self, key: K) -> None:
        """Remove a key-value pair if it exists."""
        self._storage.pop(key, None)

    def clear(self) -> None:
        """Clear the entire cache."""
        self._storage.clear()

# (str -> dict) cache
user_cache = Cache[str, dict]()
user_cache.set("user_123", {"name": "Alice", "age": 30})
print(user_cache.get("user_123"))

user_cache.remove(42)

# (int -> float) cache
price_cache = Cache[int, float]()
price_cache.set(42, 29.99)
print(price_cache.get(42))

price_cache.remove("hello world")
