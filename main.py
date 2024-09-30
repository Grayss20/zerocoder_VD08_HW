from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    url = 'https://zenquotes.io/api/random'
    response = requests.get(url)
    data = response.json()
    quote = data
    return render_template('index.html', quote=quote)


if __name__ == '__main__':
    app.run(debug=True)
