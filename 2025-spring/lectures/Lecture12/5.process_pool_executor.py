import time
from concurrent.futures import (
    ALL_COMPLETED,
    FIRST_COMPLETED,
    FIRST_EXCEPTION,
    ProcessPoolExecutor,
    as_completed,
    wait,
)


def task(id: int, delay: int, raise_error: bool = False) -> int:
    print(f"Task {id} starting with {delay}s delay")
    time.sleep(delay)
    if raise_error:
        raise ValueError(f"Task {id} failed!")
    print(f"Task {id} completed")
    return id


if __name__ == "__main__":
    print("\n** Using concurrent.futures.as_completed() **")

    with ProcessPoolExecutor(max_workers=3) as executor:
        futures = [
            executor.submit(task, 1, 3),
            executor.submit(task, 2, 1),
            executor.submit(task, 3, 2),
        ]

        print("\n== Results as tasks complete ==")
        for future in as_completed(futures):
            result = future.result()
            print(f"Task {result} returned.")

    print("\n** Using concurrent.futures.wait(return_when=ALL_COMPLETED) **")

    with ProcessPoolExecutor(max_workers=3) as executor:
        futures = [
            executor.submit(task, 1, 3),
            executor.submit(task, 2, 1),
            executor.submit(task, 3, 2),
        ]

        done, not_done = wait(futures, return_when=ALL_COMPLETED)

        print("\n== Done Tasks ==")
        for future in done:
            print(f"Result: {future.result()}")

        print("\n== Not Done Tasks ==")
        for future in not_done:
            print(f"Running: {not future.done()}")

    print("\n** Using concurrent.futures.wait(return_when=FIRST_COMPLETED) **")

    with ProcessPoolExecutor(max_workers=3) as executor:
        futures = [
            executor.submit(task, 1, 3),
            executor.submit(task, 2, 1),
            executor.submit(task, 3, 2),
        ]

        done, not_done = wait(futures, return_when=FIRST_COMPLETED)

        print("\n== Done Tasks ==")
        for future in done:
            print(f"Result: {future.result()}")

        print("\n== Not Done Tasks ==")
        for future in not_done:
            print(f"Running: {not future.done()}")

    print("\n** Using concurrent.futures.wait(return_when=FIRST_EXCEPTION) **")

    with ProcessPoolExecutor(max_workers=3) as executor:
        futures = [
            executor.submit(task, 1, 3),
            executor.submit(task, 2, 1),
            executor.submit(task, 3, 2, raise_error=True),
        ]

        done, not_done = wait(futures, return_when=FIRST_EXCEPTION)

        print("\n== Done Tasks ==")
        for future in done:
            try:
                print(f"Result: {future.result()}")
            except ValueError as e:
                print(f"Error happened: {e=} {future.exception()=}")

        print("\n== Not Done Tasks ==")
        for future in not_done:
            print(f"Running: {not future.done()}")
