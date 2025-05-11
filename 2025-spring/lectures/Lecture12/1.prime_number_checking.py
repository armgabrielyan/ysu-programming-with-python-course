import functools
import multiprocessing
import os
import threading
import time


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
def find_primes_sequential(start: int, end: int) -> list[int]:
    """Find all prime numbers in a given range sequentially."""
    return [num for num in range(start, end) if is_prime(num)]


def _check_range_for_primes_thread(
    start: int, end: int, result_list: list, lock: threading.Lock
) -> None:
    """Check a range of numbers for primes and store results in result_list."""
    local_primes = []

    # Perform computation without lock for better performance
    for num in range(start, end):
        if is_prime(num):
            local_primes.append(num)

    # Use lock only when updating the shared result list
    with lock:
        result_list.extend(local_primes)


@timer
def find_primes_multithreaded(start, end, num_threads=None):
    """Find all prime numbers in a given range using multithreading."""
    if num_threads is None:
        # For CPU-bound tasks like this, using more threads than CPU cores
        # generally doesn't improve performance, so we can use the number of CPU cores
        num_threads = os.cpu_count() or 1

    # Calculate chunk size for each thread
    chunk_size = (end - start) // num_threads

    # Create chunks with start and end points
    chunks = []
    for i in range(num_threads):
        chunk_start = start + i * chunk_size
        chunk_end = chunk_start + chunk_size if i < num_threads - 1 else end
        chunks.append((chunk_start, chunk_end))

    # Shared result list and lock for thread safety
    result_list = []
    lock = threading.Lock()

    # Create and start threads
    threads = []
    for chunk_start, chunk_end in chunks:
        thread = threading.Thread(
            target=_check_range_for_primes_thread,
            args=(chunk_start, chunk_end, result_list, lock),
        )
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Sort the results before returning
    return sorted(result_list)


def _check_range_for_primes(start: int, end: int, output: list[int]) -> None:
    """Check a range of numbers for primes and store results in output."""
    primes = [num for num in range(start, end) if is_prime(num)]
    output.extend(primes)


@timer
def find_primes_multiprocessing(start: int, end: int, num_processes: int | None = None):
    """Find all prime numbers in a given range using multiprocessing."""
    if num_processes is None:
        num_processes = multiprocessing.cpu_count()

    # Calculate chunk size for each process
    chunk_size = (end - start) // num_processes

    # Create chunks with start and end points
    chunks = []
    for i in range(num_processes):
        chunk_start = start + i * chunk_size
        chunk_end = chunk_start + chunk_size if i < num_processes - 1 else end
        chunks.append((chunk_start, chunk_end))

    # Create a shared list manager to collect results
    manager = multiprocessing.Manager()
    result_list = manager.list()

    # Create and start processes
    processes = []
    for chunk_start, chunk_end in chunks:
        p = multiprocessing.Process(
            target=_check_range_for_primes, args=(chunk_start, chunk_end, result_list)
        )
        processes.append(p)
        p.start()

    # Wait for all processes to complete
    for p in processes:
        p.join()

    # Convert manager list to regular list and sort
    return sorted(list(result_list))


def main():
    START = 0
    END = 10**7

    # Run single-threaded task
    find_primes_sequential(START, END)

    # Run multi-threaded task
    find_primes_multithreaded(START, END)

    # Run multi-processing task
    find_primes_multiprocessing(START, END)


if __name__ == "__main__":
    main()
