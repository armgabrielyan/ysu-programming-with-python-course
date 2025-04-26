import threading
import time


semaphore = threading.Semaphore(3)  # Allow 3 threads at a time


def access_resource(i):
    with semaphore:  # same as sem.acquire() + finally: sem.release()
        print(f"Thread-{i} acquired semaphore")
        time.sleep(10)
        print(f"Thread-{i} released semaphore")


threads = [threading.Thread(target=access_resource, args=(i,)) for i in range(5)]

for t in threads:
    t.start()

for t in threads:
    t.join()
