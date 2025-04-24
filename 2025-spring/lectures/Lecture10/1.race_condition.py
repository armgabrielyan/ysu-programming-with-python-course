import threading


counter = 0


def one(): return 1


def increment():
    global counter

    for _ in range(1_000_000):
        counter += one() # Critical section as a shared resource is being modified


threads = []

for _ in range(5):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()


print(f"Final counter: {counter}")
