import functools
import time
from concurrent.futures import (
    ThreadPoolExecutor,
    as_completed,
)

import httpx


def timer(func):
    """A decorator that prints the execution time of a function."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.5f} seconds")
        return result

    return wrapper


def io_bound_task(url: str) -> bytes:
    """Download content from a URL and print the status code."""
    print(f"Starting download from {url}")
    response = httpx.get(url)
    print(f"Finished downloading from {url}: Status Code {response.status_code}")
    return response.content


@timer
def handle_using_sequential(urls: list[str]):
    """A sequential task that handles a list of URLs one by one."""
    for url in urls:
        data = io_bound_task(url)
        print(f"Data downloaded from {url}: {len(data)} bytes")


@timer
def handle_using_thread_pool_executor(urls: list[str]):
    """A multi-threading task that creates and runs threads to perform IO-intensive tasks concurrently."""
    with ThreadPoolExecutor(max_workers=5) as executor:
        # Submit tasks to the executor
        future_to_url = {executor.submit(io_bound_task, url): url for url in urls}

        # Wait for futures to complete
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
                print(f"Data downloaded from {url}: {len(data)} bytes")
            except Exception as exc:
                print(f"{url} generated an exception: {exc}")


def main():
    urls = ["http://example.com", "http://example.org", "http://example.net"] * 5

    # Run single-threaded task
    handle_using_sequential(urls)

    # Run multi-threaded task
    handle_using_thread_pool_executor(urls)


if __name__ == "__main__":
    main()
