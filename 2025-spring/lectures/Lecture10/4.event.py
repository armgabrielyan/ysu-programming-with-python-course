import threading
import time


event = threading.Event()


def waiter():
    print("Waiter: Waiting for the event")
    event.wait()
    print("Waiter: The event was set!")


def setter():
    print("Setter: Sleeping before setting the event")
    time.sleep(2)
    print("Setter: Setting the event")
    event.set()


threading.Thread(target=waiter).start()
threading.Thread(target=setter).start()
