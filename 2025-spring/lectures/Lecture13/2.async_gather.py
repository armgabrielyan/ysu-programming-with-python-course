import asyncio
import time


async def work(id: int):
    print(f"Start {id}")
    await asyncio.sleep(3)
    print(f"End {id}")
    return f"Done {id}"


async def main():
    return await asyncio.gather(work(1), work(2), work(3))


if __name__ == "__main__":
    start = time.perf_counter()

    result = asyncio.run(main())
    print("Result:", result)
    
    print(f"Executed in {time.perf_counter() - start:0.2f} seconds.")
