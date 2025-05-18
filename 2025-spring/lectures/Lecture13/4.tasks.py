import asyncio


async def say_hello():
    await asyncio.sleep(1)
    print("Hello")
    return 123


async def say_world():
    await asyncio.sleep(2)
    print("World")


async def main():
    task1 = asyncio.create_task(say_hello())
    task2 = asyncio.create_task(say_world())

    print("Tasks created, now waiting...")
    # await asyncio.sleep(3) # The tasks will run in the background while we wait for 3 seconds
    res1 = await task1
    print(f"Result from task1: {res1}")
    await task2



if __name__ == "__main__":
    asyncio.run(main())
