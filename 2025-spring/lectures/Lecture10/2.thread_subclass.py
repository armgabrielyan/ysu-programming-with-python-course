import threading


class MyThread(threading.Thread):
    def __init__(self, data):
        super().__init__(name="My thread")
        self._data = data

    def run(self):
        # your custom behavior here
        print("Processing", self._data)


t2 = MyThread([1, 2, 3])
t2.start()
t2.join()
