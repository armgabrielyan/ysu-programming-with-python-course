import threading
import time


def worker(n):
    print(f"[{threading.current_thread().name}] starting work")
    time.sleep(n)
    print(f"[{threading.current_thread().name}] done")


t = threading.Thread(target=worker, args=(2,), name="Sleeper")

t.daemon = False # default; it’s non-daemon

t.start() # calls run() in new thread

print("Is alive?", t.is_alive()) # likely True
print("Thread ID", t.native_id) # thread ID

t.join(timeout=3) # wait up to 3s

print("Joined?", not t.is_alive())
