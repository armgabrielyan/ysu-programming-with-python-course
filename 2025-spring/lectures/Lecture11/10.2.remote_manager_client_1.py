# Client 1

from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


# Register the queues without callables
QueueManager.register("get_task_queue")
QueueManager.register("get_result_queue")

if __name__ == "__main__":
    # Connect to the server
    manager = QueueManager(address=("localhost", 50000), authkey=b"secret")
    manager.connect()

    task_queue = manager.get_task_queue()
    result_queue = manager.get_result_queue()

    # Use the queues as if local
    task_queue.put("Task A")
    print("Task sent")

    result = result_queue.get()
    print("Result received:", result)
