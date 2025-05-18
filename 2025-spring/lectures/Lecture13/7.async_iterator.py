import asyncio


class AsyncCounter:
    def __init__(self, limit):
        self._limit = limit
        self._counter = 0

    def __aiter__(self) -> "AsyncCounter":
        return self

    async def __anext__(self) -> int:
        if self._counter < self._limit:
            self._counter += 1
            await asyncio.sleep(1)
            return self._counter
        else:
            raise StopAsyncIteration


async def main():
    async for number in AsyncCounter(5):
        print(f"Got number: {number}")

    print("Iteration complete")


asyncio.run(main())
