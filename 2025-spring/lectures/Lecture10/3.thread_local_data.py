import threading
import time
import random


# Thread-local data storage
thread_local_storage = threading.local()


def worker(thread_id: int) -> None:
    # Initialize data for this specific thread
    thread_local_storage.value = thread_id * 10
    thread_local_storage.random_sleep = random.randint(1, 5)

    print(f"Thread-{thread_id}: Initialized local value to {thread_local_storage.value}")
    time.sleep(thread_local_storage.random_sleep)

    # Simulate some processing
    process_data(thread_id)

def process_data(thread_id: int) -> None:
    current_value = thread_local_storage.value
    sleep_time = thread_local_storage.random_sleep

    print(f"Thread-{thread_id}: Processing data. Value = {current_value}, Sleep = {sleep_time:.2f}")
    # Modify the thread-local data (only affects this thread)
    thread_local_storage.value += 1
    print(f"Thread-{thread_id}: Incremented local value to {thread_local_storage.value}")


threads = []

for i in range(3):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Main: All threads finished.")

# Trying to access from the main thread
try:
    print(f"Main: Accessing value: {thread_local_storage.value}")
except AttributeError:
    print("Main: 'value' attribute not set for the main thread.")
