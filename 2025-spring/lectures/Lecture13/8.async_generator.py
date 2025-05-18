import asyncio
import random


async def async_data_stream(count: int):
    """Simulate an asynchronous data stream."""
    for i in range(count):
        await asyncio.sleep(random.uniform(0.05, 0.2))
        yield f"Data chunk {i + 1}"


async def process_stream():
    print("Starting to process data stream...")

    async for data in async_data_stream(5):
        print(f"Processing: {data}")
        await asyncio.sleep(0.5)

    print("Stream processing complete")

    results = [data async for data in async_data_stream(5)]

    print(f"Comprehension results: {results}")


asyncio.run(process_stream())
