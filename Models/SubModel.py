

class SubModel:
    # @contract(title=str, ulr=str, score='str|None')
    def __init__(self, title, url, score, popularity, subreddit, subreddit_subscribers):
        self._title = title
        self._url = url
        self._score = score
        self._popularity = popularity
        self._subreddit = subreddit
        self._subreddit_subscribers = subreddit_subscribers

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
