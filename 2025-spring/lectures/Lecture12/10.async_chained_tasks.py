import asyncio
import random
import time


async def fetch_data(source_id: int) -> str:
    delay = random.randint(1, 5)
    print(f"[Fetch] Starting fetch from source {source_id} with delay {delay} seconds")
    await asyncio.sleep(delay)
    data = f"data_from_{source_id}"
    print(f"[Fetch] Done fetching from source {source_id}")
    return data


async def process_data(data: str) -> str:
    delay = random.randint(1, 10)
    print(f"[Process] Processing {data} with delay {delay} seconds")
    await asyncio.sleep(delay)
    result = data.upper()
    print(f"[Process] Finished processing {data}")
    return result


async def save_result(result: str):
    delay = random.randint(1, 3)
    print(f"[Save] Saving {result} with delay {delay} seconds")
    await asyncio.sleep(random.randint(1, 3))
    print(f"[Save] Saved {result}")


async def handle_pipeline(source_id: int) -> None:
    start = time.perf_counter()
    
    data = await fetch_data(source_id)
    processed = await process_data(data)
    await save_result(processed)

    print(f"[Pipeline] Completed pipeline for source {source_id} in {time.perf_counter() - start:.2f} seconds")


async def main():
    # Run 5 pipelines in parallel
    await asyncio.gather(*(handle_pipeline(i) for i in range(5)))


if __name__ == "__main__":
    start = time.perf_counter()

    asyncio.run(main())

    # The runtime of main() will be equal to the maximum runtime of the tasks that it gathers together and schedules. 
    print(f"\nAll tasks completed in {time.perf_counter() - start:.2f} seconds.")
