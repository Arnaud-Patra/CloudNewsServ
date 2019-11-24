import asyncio
from aiohttp import ClientSession


async def hello(url_to_fetch):
    async with ClientSession() as session:
        async with session.get(url_to_fetch) as response:

            response = await response.read()

            print("response : " + response.decode())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    url = "https://www.reddit.com/r/worldnews/top.json?limit=1"

    print('starting loop ...')

    loop.run_until_complete(hello(url))

    print('after loop.')


