import asyncio


async def greet():
    print("Hello")
    await asyncio.sleep(1)
    print("World")


async def main():
    loop = asyncio.get_running_loop()
    print(f"Current loop: {loop}")
    task = loop.create_task(greet())
    print("Task created, now waiting...")
    # await task


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
try:
    loop.run_until_complete(main())
finally:
    print("Closing loop")
    loop.close()
