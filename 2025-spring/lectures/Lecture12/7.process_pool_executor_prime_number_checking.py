import functools
import time
from concurrent.futures import ProcessPoolExecutor


def timer(func):
    """A decorator that prints the execution time of a function."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.5f} seconds")
        return result

    return wrapper


def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


@timer
def find_primes_sequential(numbers: list[int]) -> list[int]:
    """Find all prime numbers in a given list sequentially."""
    return [num for num in numbers if is_prime(num)]


@timer
def find_primes_multiprocessing(numbers: list[int], num_processes: int | None = None):
    """Find all prime numbers in a given range using multiprocessing."""
    primes = []
    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        for number, prime in zip(numbers, executor.map(is_prime, numbers)):
            if prime:
                primes.append(number)
    return sorted(primes)


def main():
    NUMS = [
        112272535095293,
        112582705942171,
        115280095190773,
        115797848077099,
        1099726899285419,
        1099726899285433,
        115280095190789
    ]

    # Run single-threaded task
    find_primes_sequential(NUMS)

    # Run multi-processing task
    find_primes_multiprocessing(NUMS)


if __name__ == "__main__":
    main()
