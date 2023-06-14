import asyncio

loop = asyncio.get_event_loop()

actions = []


async def drive():
    print('driving')

async def main():
    loop.create_task(drive())
    await asyncio.sleep(3)
    loop.create_task(drive())

loop.run_until_complete(main())
