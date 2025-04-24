import multiprocessing
import time


def is_prime(n: int) -> bool:
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


def check_range_for_primes(start: int, end: int, output: list[int]) -> None:
    """Check a range of numbers for primes and store results in output."""
    primes = [num for num in range(start, end) if is_prime(num)]
    output.extend(primes)


def find_primes_multiprocessing(start: int, end: int, num_processes: int | None = None):
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
            target=check_range_for_primes,
            args=(chunk_start, chunk_end, result_list)
        )
        processes.append(p)
        p.start()
    
    # Wait for all processes to complete
    for p in processes:
        p.join()
    
    # Convert manager list to regular list and sort
    return sorted(list(result_list))


START = 0
END = 10**7


if __name__ == "__main__":
    start_time = time.time()
    primes = find_primes_multiprocessing(START, END)
    exec_time = time.time() - start_time
    print(f"Multiprocessing: Found {len(primes)} primes in {exec_time:.2f} seconds")
