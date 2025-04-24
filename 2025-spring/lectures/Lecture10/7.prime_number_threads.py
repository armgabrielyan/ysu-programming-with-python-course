import os
import threading
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


def check_range_for_primes(start: int, end: int, result_list: list, lock: threading.Lock) -> None:
    local_primes = []
    
    # Perform computation without lock for better performance
    for num in range(start, end):
        if is_prime(num):
            local_primes.append(num)
    
    # Use lock only when updating the shared result list
    with lock:
        result_list.extend(local_primes)


def find_primes_multithreaded(start, end, num_threads=None):
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
            target=check_range_for_primes,
            args=(chunk_start, chunk_end, result_list, lock)
        )
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    # Sort the results before returning
    return sorted(result_list)


START = 0
END = 10**7


if __name__ == "__main__":
    start_time = time.time()
    thread_primes = find_primes_multithreaded(START, END)
    thread_time = time.time() - start_time
    print(f"Multithreaded: Found {len(thread_primes)} primes in {thread_time:.2f} seconds")
