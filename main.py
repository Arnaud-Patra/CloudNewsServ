import logging

from flask import Flask

from fetcher import main


# !! deploy : gcloud app deploy

# flask used as a API
app = Flask(__name__)

@app.route('/get_france')
def get_france():
    articles = main(['FRANCE'])
    return articles


@app.route('/get_tech')
def get_tech():
    articles = main(['TECH'])
    return articles


@app.route('/get_reddit_news')
def get_reddit_news():
    articles = main(['REDDIT_NEWS'])
    return articles

@app.route('/helloworld')
def helloworld():
    return "hello"


if __name__ == '__main__':
    # app.run(port='8000')
    app.run(host='127.0.0.1', port=8080, debug=True)
