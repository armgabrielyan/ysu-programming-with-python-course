from multiprocessing import Process, current_process
import os
import time


def info(title):
    print(f"\n[{title}]")
    print('Module name:', __name__)
    print('Parent process ID:', os.getppid())
    print('Current process ID:', os.getpid())


def worker(n):
    info(current_process().name + " starting work")
    time.sleep(n)
    print(f"[{current_process().name}] done")


if __name__ == '__main__':
    info("Main process")
    p = Process(target=worker, args=(2,), name="Sleeper")
    p.daemon = False  # default is non-daemon

    p.start()

    print("\nIs alive?", p.is_alive()) # likely True
    print("Process ID", p.pid) # child process ID

    p.join(timeout=3) # wait up to 3s

    print("Joined?", not p.is_alive())
