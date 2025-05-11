import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


def slow_square(n: int) -> int:
    time.sleep(1)
    return n * n


def slow_work(x):
    time.sleep(5)
    return x


if __name__ == "__main__":
    # Submit
    with ProcessPoolExecutor(max_workers=1) as executor:
        future = executor.submit(pow, 2, 10)
        print("Result from submit:", future.result())

    # Map
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(slow_square, [1, 2, 3, 4, 5])
        print("Results from map:", results)
        for result in results:
            print("Result from map:", result)

    # Shutdown
    with ThreadPoolExecutor(max_workers=1) as executor:
        # First task starts immediately
        f1 = executor.submit(slow_work, 1)
        # Second task is queued
        f2 = executor.submit(slow_work, 2)

        # Shutdown with cancel_futures=True cancels the queued f2
        executor.shutdown(wait=False, cancel_futures=True)

        print("f1 result (may complete):", f1.result(timeout=10))
        print("f2 cancelled:", f2.cancelled())
