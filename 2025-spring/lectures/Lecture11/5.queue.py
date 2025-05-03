from multiprocessing import Process, Queue
import queue
import time
import random


def worker(task_queue: Queue, result_queue: Queue, worker_id: int):
    while not task_queue.empty():
        try:
            task = task_queue.get_nowait()
        except queue.Empty:
            break
        
        print(f"[Worker-{worker_id}] Processing: {task}")
        
        time.sleep(random.randint(1, 5))  # Simulate work

        result = f"Result of {task} by Worker-{worker_id}"
        result_queue.put(result)


if __name__ == "__main__":
    tasks = [f"Task-{i}" for i in range(10)]
    task_queue = Queue()
    result_queue = Queue()

    for task in tasks:
        task_queue.put(task)

    workers = []
    for i in range(3):
        p = Process(target=worker, args=(task_queue, result_queue, i))
        workers.append(p)
        p.start()

    for p in workers:
        p.join()

    print("\nAll results:")
    while not result_queue.empty():
        print(result_queue.get())
