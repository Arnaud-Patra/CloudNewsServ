import asyncio
import json
import requests

from aiohttp import ClientSession

from Models.SubModel import newsapi_org_to_model, reddit_to_model
from enum_ressources.urls import reddit_news, categories


# tuto from https://pawelmhm.github.io/asyncio/python/aiohttp/2016/04/22/asyncio-aiohttp.html


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


def fetch_cat(category_keys):
    loop = asyncio.get_event_loop()

    # urls = ["https://www.reddit.com/r/worldnews/top.json?limit=1", "https://www.reddit.com/r/news/top.json?limit=1"]

    # todo : select good category
    for key in category_keys:
        api = categories[key]
        # print("api used : " + api)
        # only one category at the time now
    urls = []
    for url_key in api:
        urls.append(api[url_key])
        print(url_key)

    # parse url to fetch TODO : put that in a function
    if category_keys != ['FRANCE']:
        urls[:] = [url + "top.json?limit=3" for url in urls]
        # for url in urls:
        #     url = url + "top.json?limit=3"
        #     print(url)

    # run fetches
    future = asyncio.ensure_future(run(urls))

    responses = loop.run_until_complete(future)

    return responses


if __name__ == '__main__':
    loop_test = asyncio.get_event_loop()

    # urls_test = ["https://www.reddit.com/r/worldnews/top.json?limit=1", "https://www.reddit.com/r/news/top.json?limit=1"]

    # category_keys = ['FRANCE']
    category_keys = ['REDDIT_NEWS']

    responses_test = fetch_cat(category_keys)

    # decode response to json
    responses_test[:] = [i.decode("utf-8") for i in responses_test]
    json_response = [json.loads(resp) for resp in responses_test]

    print(">>> response :")
    print(json_response)

    # Parse response.
    if category_keys == ['FRANCE']:
        newsapi_org_to_model(json_response)
    else:
        reddit_to_model(json_response)

    # # run fetches
    # future_test = asyncio.ensure_future(run(urls_test))
    # responses_test = loop_test.run_until_complete(future_test)
