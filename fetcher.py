import asyncio
import json
import requests

from aiohttp import ClientSession

from Models.SubModel import newsapi_org_to_model, reddit_to_model, popularity_calculator
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
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # loop = asyncio.get_event_loop()  # crash here

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


def serialise_submodel(submodel):
    dictionnairy = {
        'title': submodel.title,
        'url': submodel.url,
        'score': submodel.score,
        'subreddit': submodel.subreddit,
        'subreddit_subscribers': submodel.subreddit_subscribers,
        'popularity': submodel.popularity,
        'source': submodel.source,
        'description': submodel.description,
    }

    return dictionnairy


def main(category_keys):
    respsonses = fetch_cat(category_keys)

    # decode response to json
    respsonses[:] = [i.decode("utf-8") for i in respsonses]
    json_response = [json.loads(resp) for resp in respsonses]

    # Parse response.
    if category_keys == ['FRANCE']:
        articles = newsapi_org_to_model(json_response)
    else:
        articles = reddit_to_model(json_response)
        popularity_calculator(articles)

    #todo : parse articles from [dict,dict,dict] to dict{dict, dict...}

    art_dict = {'articles': []}
    for article in articles:
        art_dict['articles'].append(serialise_submodel(article))

    return art_dict


if __name__ == '__main__':
    # loop_test = asyncio.get_event_loop() #useless?

    # urls_test = ["https://www.reddit.com/r/worldnews/top.json?limit=1", "https://www.reddit.com/r/news/top.json?limit=1"]

    # category_keys = ['FRANCE']
    category_keys_test = ['REDDIT_NEWS']

    responses_test = fetch_cat(category_keys_test)

    # decode response to json
    responses_test[:] = [i.decode("utf-8") for i in responses_test]
    json_response = [json.loads(resp) for resp in responses_test]

    # Parse response.
    if category_keys_test == ['FRANCE']:
        articles_modeled_test = newsapi_org_to_model(json_response)
    else:
        articles_modeled_test = reddit_to_model(json_response)


