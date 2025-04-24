import time


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def find_primes_sequential(start: int, end: int) -> list[int]:
    return [num for num in range(start, end) if is_prime(num)]


START = 0
END = 10**7


if __name__ == "__main__":
    start_time = time.time()
    sequential_primes = find_primes_sequential(START, END)
    sequential_time = time.time() - start_time
    print(f"Sequential: Found {len(sequential_primes)} primes in {sequential_time:.2f} seconds")
