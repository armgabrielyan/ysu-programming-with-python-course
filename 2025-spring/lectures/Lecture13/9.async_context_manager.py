import asyncio


class AsyncResource:
    async def __aenter__(self):
        print("Acquiring resource asynchronously...")
        await asyncio.sleep(1)
        print("Resource acquired")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Releasing resource asynchronously...")
        await asyncio.sleep(0.5)
        print("Resource released")
        # Return False to propagate exceptions, True to suppress them
        return False

    async def use_resource(self):
        print("Using the resource")
        await asyncio.sleep(0.5)


async def main():
    async with AsyncResource() as resource:
        await resource.use_resource()
        print("Still in the context")

    print("Outside the context")


asyncio.run(main())
