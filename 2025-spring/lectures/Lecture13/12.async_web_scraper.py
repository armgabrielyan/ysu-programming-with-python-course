import asyncio
import functools
import time

import httpx


def timer(func):
    """A decorator that prints the execution time of an async or sync function."""

    if asyncio.iscoroutinefunction(func):

        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            start_time = time.time()
            result = await func(*args, **kwargs)
            end_time = time.time()
            print(
                f"Function '{func.__name__}' executed in {end_time - start_time:.5f} seconds"
            )
            return result

        return async_wrapper

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(
            f"Function '{func.__name__}' executed in {end_time - start_time:.5f} seconds"
        )
        return result

    return wrapper


def io_bound_task(url: str) -> bytes:
    """Download content from a URL and print the status code."""
    print(f"Starting download from {url}")
    response = httpx.get(url)
    print(f"Finished downloading from {url}: Status Code {response.status_code}")
    return response.content


async def async_io_bound_task(url: str, client: httpx.AsyncClient) -> bytes:
    """Asynchronous download content from a URL and print the status code."""
    print(f"Starting download from {url}")
    response = await client.get(url)
    print(f"Finished downloading from {url}: Status Code {response.status_code}")
    return response.content


@timer
def handle_using_sequential(urls: list[str]):
    """A sequential task that handles a list of URLs one by one."""
    for url in urls:
        io_bound_task(url)


@timer
async def handle_using_asyncio(urls: list[str]):
    """Handle a list of URLs concurrently using asyncio and httpx.AsyncClient."""
    async with httpx.AsyncClient() as client:
        tasks = [async_io_bound_task(url, client) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        for url, result in zip(urls, results):
            if isinstance(result, BaseException):
                print(f"{url} generated an exception: {result}")
            else:
                print(f"Data downloaded from {url}: {len(result)} bytes")


def main():
    urls = ["http://example.com", "http://example.org", "http://example.net"] * 5

    # Run single-threaded task
    handle_using_sequential(urls)

    # Run single-threaded with async io
    asyncio.run(handle_using_asyncio(urls))


if __name__ == "__main__":
    main()
