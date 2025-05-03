import multiprocessing


def increment(shared_counter, lock):
    for _ in range(10_000):
        with lock:
            shared_counter.value += 1


if __name__ == "__main__":
    # Create a shared integer variable, "i" means integer
    counter = multiprocessing.Value("i", 0)
    
    # Create a lock to synchronize access to the shared variable
    lock = multiprocessing.Lock()

    processes = []
    for _ in range(10):
        p = multiprocessing.Process(target=increment, args=(counter, lock))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f"Final counter value: {counter.value}")
