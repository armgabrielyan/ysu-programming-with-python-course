import asyncio


async def long_running_task():
    print("Task started")
    for i in range(5):
        print(f"Working... step {i}")
        await asyncio.sleep(1)
    print("Task completed")
    return "Task result"


async def main():
    task = asyncio.create_task(long_running_task())

    print(f"Task done? {task.done()}")

    # task.result()

    try:
        result = await asyncio.wait_for(task, timeout=2)
        print(f"Got result: {result}")
    except asyncio.TimeoutError:
        print("Task took too long, but continues running")

    print(f"Task done? {task.done()}")
    print(f"Task cancelled? {task.cancelled()}")


if __name__ == "__main__":
    asyncio.run(main())
