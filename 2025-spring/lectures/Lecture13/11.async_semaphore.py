import asyncio
import random


async def limited_worker(name: str, semaphore: asyncio.Semaphore) -> None:
    """A worker function that simulates a task with a semaphore."""
    async with semaphore:
        print(f"{name} is running")
        await asyncio.sleep(random.uniform(1, 3))
        print(f"{name} is done")


async def main():
    semaphore = asyncio.Semaphore(2) # Allow up to 2 tasks at once

    tasks = [limited_worker(f"Task-{i}", semaphore) for i in range(5)]

    await asyncio.gather(*tasks)


asyncio.run(main())
