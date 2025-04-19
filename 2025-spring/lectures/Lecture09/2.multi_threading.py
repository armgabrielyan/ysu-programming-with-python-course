import time
import threading


def slow(delay: int) -> int:
    time.sleep(delay)  # Simulate a blocking I/O operation
    return 42


def do_work(name: str, delay: int, results: list[int]) -> None:
    print(f"[{name}] Starting work...")
    result = slow(delay) # Simulate slow work
    results[delay - 1] = result  # Store the result
    print(f"[{name}] Finished after {delay} seconds")


def main():
    threads = []
    results = [None] * 3 # Shared data for storing results. It will be filled by the threads.

    for i in range(3):
        t = threading.Thread(target=do_work, args=(f"Thread-{i + 1}", i + 1, results))
        threads.append(t)
        t.start()

    for index, t in enumerate(threads):
        t.join()

        print(f"Thread-{index + 1} has finished with result: {results[index]}")

    print("All threads have finished.")


if __name__ == '__main__':
    start = time.perf_counter()
    main()
    print(f"Execution completed in {time.perf_counter() - start} seconds")
