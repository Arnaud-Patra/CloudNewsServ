def newsapi_org_to_model(responses_json_list):
    model_list = []
    for responses_json in responses_json_list:
        for article in responses_json['articles']:
            model = SubModel(title=article['title'], url=article['url'], source=article['source'],
                             description=article['description'])

            model_list.append(model)

    return model_list


def reddit_to_model(responses_json_list):
    model_list = []
    for subreddit in responses_json_list:
        for sub in subreddit['data']['children']:
            sub_data = sub['data']
            model = SubModel(title=sub_data['title'], url=sub_data['url'], score=sub_data['score'],subreddit=sub_data['subreddit'],
                             subreddit_subscribers=sub_data['subreddit_subscribers'])

            model_list.append(model)

    return model_list


def popularity_calculator(articles):
    for article in articles:
        article.popularity = 1000 * article.score / article.subreddit_subscribers


class SubModel:
    # @contract(title=str, ulr=str, score='str|None')
    def __init__(self, title, url, score=None, popularity=None, source=None, subreddit=None, subreddit_subscribers=None,
                 description=None):
        self._title = title
        self._url = url
        self._score = score
        self._popularity = popularity
        self._source = source
        self._subreddit = subreddit
        self._subreddit_subscribers = subreddit_subscribers
        self._description = description

    # TODO : add getter and setters

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, source):
        self._source = source

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def popularity(self):
        return self._popularity

    @popularity.setter
    def popularity(self, popularity):
        self._popularity = popularity

    @property
    def subreddit(self):
        return self._subreddit

    @subreddit.setter
    def subreddit(self, subreddit):
        self._subreddit = subreddit

    @property
    def subreddit_subscribers(self):
        return self._subreddit_subscribers

    @subreddit_subscribers.setter
    def subreddit_subscribers(self, subreddit_subscribers):
        self._subreddit_subscribers = subreddit_subscribers
