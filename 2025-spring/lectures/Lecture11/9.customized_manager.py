from multiprocessing.managers import BaseManager
from multiprocessing import Process


class Counter:
    def __init__(self):
        self._value = 0

    def increment(self):
        self._value += 1

    def get(self) -> int:
        return self._value


# Create a custom manager
class MyManager(BaseManager):
    pass


# Register the Counter class so it can be shared
MyManager.register("Counter", Counter)


def worker(counter):
    for _ in range(10_000):
        counter.increment()


if __name__ == "__main__":
    with MyManager() as manager:
        counter = manager.Counter() # Get a proxy to the shared Counter

        processes = [Process(target=worker, args=(counter,)) for _ in range(10)]

        for p in processes:
            p.start()
        for p in processes:
            p.join()

        print("Final count:", counter.get())
