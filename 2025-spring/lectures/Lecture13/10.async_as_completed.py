import asyncio
import random
import time


def blocking_task(name: str, delay: float) -> str:
    """Simulates a blocking function."""
    time.sleep(delay)
    return f"Blocking task {name} finished after {delay}s"


async def main():
    delays = [random.uniform(0.5, 2.0) for _ in range(3)]
    tasks = [
        asyncio.to_thread(blocking_task, name, delay)
        for name, delay in zip(["A", "B", "C"], delays)
    ]

    for future in asyncio.as_completed(tasks):
        result = await future
        print(result)


asyncio.run(main())
