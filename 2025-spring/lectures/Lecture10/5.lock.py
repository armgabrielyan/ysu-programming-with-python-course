import threading


counter = 0

lock = threading.Lock()  # Create a lock object


def one(): return 1


def increment():
    global counter

    for _ in range(1_000_000):
        with lock:
            counter += one() # Critical section as a shared resource is being modified


threads = []

for _ in range(5):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()


print(f"Final counter: {counter}")
