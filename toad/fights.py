import asyncio

from utils import start_fight


async def main():
    results = await asyncio.gather(start_fight(), start_fight())
    for result in results:
        print(f'Number of victories:\n{result}')


asyncio.run(main())
