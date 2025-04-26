import functools
import sys
import math
import time
from threading import Thread
from multiprocessing import Process

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


def cpu_bound_task(num: int) -> int:
    """A compute-intensive task that calculates the factorial of a number."""
    return math.factorial(num)


@timer
def handle_using_sequential(nums):
    """A sequential task that handles a list of numbers one by one."""
    for num in nums:
        cpu_bound_task(num)


@timer
def handle_using_multi_threading(nums):
    """A multi-threading task that creates and runs threads to perform compute-intensive tasks concurrently."""
    threads = []

    for num in nums:
        thread = Thread(target=cpu_bound_task, args=(num,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


@timer
def handle_using_multi_processing_(nums):
    """A multi-processing task that creates and runs processes to perform compute-intensive tasks concurrently."""
    processes = []

    for num in nums:
        process = Process(target=cpu_bound_task, args=(num,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


def main():
    print(f"Python Version: {sys.version}")

    status = None

    if sys.version_info >= (3, 13):
        status = sys._is_gil_enabled()
    if status is None:
        print("GIL cannot be disabled in this version of Python")
    if status == 0:
        print("GIL is currently disabled")
    if status == 1:
        print("GIL is currently active")

    nums = [5 * 10 ** 5 + i for i in range(5)]

    # Run single-threaded task
    handle_using_sequential(nums)

    # Run multi-threaded task
    handle_using_multi_threading(nums)

    # Run multi-processing task
    handle_using_multi_processing_(nums)


if __name__ == "__main__":
    main()
