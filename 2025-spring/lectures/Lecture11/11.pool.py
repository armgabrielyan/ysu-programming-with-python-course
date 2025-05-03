from multiprocessing import Pool, TimeoutError
import time
import os
import math


def factorial(n):
    """Calculate the factorial of n"""
    return math.factorial(n)


def slow_factorial(n):
    """Calculate factorial with artificial delay"""
    time.sleep(1)  # Add a delay to simulate complex computation
    return factorial(n)


if __name__ == "__main__":
    # start 4 worker processes
    with Pool(processes=4) as pool:
        # print factorials of [1, 2, 3, ..., 10]
        print("Calculating factorials using pool.map:")
        print(pool.map(factorial, range(1, 11)))

        # print same factorials in arbitrary order
        print("\nCalculating factorials using pool.imap_unordered:")
        for i in pool.imap_unordered(factorial, range(1, 11)):
            print(i)

        # evaluate "factorial(15)" asynchronously
        print("\nCalculating factorial(15) asynchronously:")
        res = pool.apply_async(factorial, (15,))  # runs in *only* one process
        print(f"factorial(15) = {res.get(timeout=1)}")  # prints factorial of 15

        # evaluate "os.getpid()" asynchronously
        print("\nGetting process ID asynchronously:")
        res = pool.apply_async(os.getpid, ())  # runs in *only* one process
        print(f"Process ID: {res.get(timeout=1)}")  # prints the PID of that process

        # launching multiple evaluations asynchronously *may* use more processes
        print("\nGetting multiple process IDs asynchronously:")
        multiple_results = [pool.apply_async(os.getpid, ()) for i in range(4)]
        process_ids = [res.get(timeout=1) for res in multiple_results]
        print(f"Process IDs: {process_ids}")
        print(f"Number of unique processes: {len(set(process_ids))}")

        # demonstrate parallel computation advantage
        print("\nDemonstrating parallel vs. sequential computation:")
        numbers = [20, 21, 22, 23]

        # Sequential calculation
        start_time = time.perf_counter()
        for num in numbers:
            slow_factorial(num)
            # factorial(num)
        sequential_time = time.perf_counter() - start_time
        print(f"Sequential calculation time: {sequential_time:.2f} seconds")

        # Parallel calculation
        start_time = time.perf_counter()
        results = [pool.apply_async(slow_factorial, (num,)) for num in numbers]
        for res in results:
            res.get()
        parallel_time = time.perf_counter() - start_time
        print(f"Parallel calculation time: {parallel_time:.2f} seconds")
        print(f"Speedup: {sequential_time / parallel_time:.2f}x")

        # make a single worker sleep for 5 seconds to demonstrate timeout
        print("\nDemonstrating timeout handling:")
        res = pool.apply_async(time.sleep, (5,))
        # res.successful()
        try:
            print(res.get(timeout=1))
        except TimeoutError:
            print("We lacked patience and got a multiprocessing.TimeoutError")

        print("For the moment, the pool remains available for more work")

    # exiting the 'with'-block has stopped the pool
    print("Now the pool is closed and no longer available")
