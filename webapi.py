from flask import Flask

from google.cloud import vision

vision_client = vision.Client()

# flask used as a API
app = Flask(__name__)


@app.route('/get')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    # app.run(port='8000')
    app.run(host='127.0.0.1', port=8080, debug=True)

