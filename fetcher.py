import asyncio
from aiohttp import ClientSession


# tuto from https://pawelmhm.github.io/asyncio/python/aiohttp/2016/04/22/asyncio-aiohttp.html
from enum.urls import reddit_news


async def fetch(url, session):
    async with session.get(url) as response:
        return await response.read()


async def run(urls):
    tasks = []

    # Fetch all responses within one Client session,
    # keep connection alive for all requests.
    async with ClientSession() as session:
        for url in urls:
            task = asyncio.ensure_future(fetch(url, session))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)
        # you now have all response bodies in this variable
        return responses


def fetch_cat(category_key):
    loop = asyncio.get_event_loop()

    urls = ["https://www.reddit.com/r/worldnews/top.json?limit=1", "https://www.reddit.com/r/news/top.json?limit=1"]

    #todo : select good category
    for key in reddit_news:
        print(key, '->', reddit_news[key])

    # run fetches
    future = asyncio.ensure_future(run(urls))

    responses = loop.run_until_complete(future)

    return responses



if __name__ == '__main__':
    loop_test = asyncio.get_event_loop()

    urls_test = ["https://www.reddit.com/r/worldnews/top.json?limit=1", "https://www.reddit.com/r/news/top.json?limit=1"]
    # run fetches
    future_test = asyncio.ensure_future(run(urls_test))
    responses_test = loop_test.run_until_complete(future_test)

    print(responses_test)
