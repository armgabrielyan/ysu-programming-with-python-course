import time


def do_work(name: str, delay: int) -> None:
    print(f"[{name}] Starting work...")
    time.sleep(delay)
    print(f"[{name}] Finished after {delay} seconds")


def main():
    for i in range(3):
        do_work(f"Thread-{i + 1}", i + 1)

    print("All works have finished.")

if __name__ == '__main__':
    start = time.perf_counter()
    main()
    print(f"Execution completed in {time.perf_counter() - start} seconds")
