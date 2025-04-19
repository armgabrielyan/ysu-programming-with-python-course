import time
import multiprocessing


def slow() -> int:
    time.sleep(3)  # Simulate a blocking I/O operation
    return 42


def do_work(name: str, delay: int) -> None:
    print(f"[{name}] Starting work...")
    slow()  # Simulate slow work
    print(f"[{name}] Finished after {delay} seconds")


def main():
    processes = []

    for i in range(3):
        p = multiprocessing.Process(target=do_work, args=(f"Process-{i + 1}", i + 1))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("All processes have finished.")


if __name__ == '__main__':
    start = time.perf_counter()
    main()
    print(f"Execution comleted in {time.perf_counter() - start} seconds")
