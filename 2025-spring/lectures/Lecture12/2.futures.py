import concurrent.futures
import time


def slow_function(delay: int) -> int:
    """Simulate a slow function that takes 'delay' to complete."""
    time.sleep(delay)
    return 42


def done_callback(future: concurrent.futures.Future) -> None:
    print(f"Callback: future is done, result = {future.result()}")


print("Submit a future\n")

with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
    future = executor.submit(slow_function, 2)

    future.add_done_callback(done_callback)

    print("Future running:", future.running())
    print("Future done:", future.done())

    result = future.result(timeout=3)

    print("Result:", result)

    print("Future done after result():", future.done())
    print("Future cancelled:", future.cancelled())
    print("Future exception:", future.exception())


print("\nWith a timeout\n")

# With a timeout
with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
    future = executor.submit(slow_function, 5)

    try:
        result = future.result(
            timeout=3
        )  # This will raise a TimeoutError as the function takes 5 seconds
        print("Result:", result)
    except concurrent.futures.TimeoutError:
        print("The function took too long!")
    except Exception as e:
        print("An error occurred:", e)


print("\nCancel the future\n")

# Cancel the future
with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
    # Submit a first task that will occupy the worker
    blocker = executor.submit(slow_function, 10)

    # Submit the second task (won't start immediately)
    future = executor.submit(slow_function, 5)

    # Try cancelling the second future immediately
    cancelled = future.cancel()
    print("Cancelled:", cancelled)
    print("Future cancelled():", future.cancelled())
    print("Future done():", future.done())
