# Client 2
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


# Register both queues without callables
QueueManager.register("get_task_queue")
QueueManager.register("get_result_queue")

if __name__ == "__main__":
    manager = QueueManager(address=("localhost", 50000), authkey=b"secret")
    manager.connect()

    task_queue = manager.get_task_queue()
    result_queue = manager.get_result_queue()

    while True:
        try:
            task = task_queue.get(timeout=5) # Wait for a task for 5 seconds
            print(f"Processing task: {task}")
            result = f"{task} done"
            result_queue.put(result)
            print(f"Wrote result: {result}")
        except Exception:
            print("No more tasks. Exiting.")
            break
