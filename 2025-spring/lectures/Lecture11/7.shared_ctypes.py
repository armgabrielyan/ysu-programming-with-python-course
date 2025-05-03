import ctypes
from multiprocessing import Process
from multiprocessing.sharedctypes import Array, Value


# Define custom structure
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double), ("y", ctypes.c_double)]


def update_points(counter, points, dx, dy):
    for i in range(len(points)):
        with points.get_lock():
            points[i].x += dx
            points[i].y += dy
    with counter.get_lock():
        counter.value += 1
        print(f"[Process] Counter: {counter.value}")
    with points.get_lock():
        print("Updated points:", [(p.x, p.y) for p in points])


if __name__ == "__main__":
    initial_points = [Point(0.0, 0.0) for _ in range(3)]

    # Shared counter and shared array of Points
    counter = Value(ctypes.c_int, 0)
    points = Array(Point, initial_points)

    # Movements to apply in different processes
    deltas = [(1, 1), (2, 0), (0, -1)]

    processes = []
    for dx, dy in deltas:
        p = Process(target=update_points, args=(counter, points, dx, dy))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("\nFinal Counter:", counter.value)
    print("Final Points:")
    for p in points:
        print(f"\t({p.x}, {p.y})")
