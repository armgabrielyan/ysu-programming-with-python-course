import threading
import queue
import time
import random


# Thread-safe queue
task_queue = queue.Queue(maxsize=10)


def producer():
    for i in range(5):
        item = f"Task {i}"
        
        task_queue.put(item)  # Will block if queue is full
        
        print(f"Produced: {item}")
        
        time.sleep(random.random())


def consumer():
    while item := task_queue.get():
        # item = task_queue.get()  # Will block if queue is empty
        # if item is None:
        #     break

        print(f"Consumed: {item}")
        
        time.sleep(random.random() * 2)
        
        task_queue.task_done()  # Mark task as done


# Start consumer thread
consumer_thread = threading.Thread(target=consumer)
consumer_thread.start()

# Start producer thread
producer_thread = threading.Thread(target=producer)
producer_thread.start()

# Wait for producer to finish
producer_thread.join()

# Wait for all tasks to be processed
task_queue.join()

# Stop consumer
task_queue.put(None)
consumer_thread.join()
