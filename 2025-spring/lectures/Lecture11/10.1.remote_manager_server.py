# Server
from multiprocessing.managers import BaseManager
from multiprocessing import Queue

# Queues to share
task_queue = Queue()
result_queue = Queue()


class QueueManager(BaseManager):
    pass


# Register the queues to be shared
QueueManager.register("get_task_queue", callable=lambda: task_queue)
QueueManager.register("get_result_queue", callable=lambda: result_queue)

if __name__ == "__main__":
    manager = QueueManager(address=("localhost", 50000), authkey=b"secret")
    server = manager.get_server()
    print("Server started at port 50000")
    server.serve_forever()
