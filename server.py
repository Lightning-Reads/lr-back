from flask import Flask
from flask import request
from flask import jsonify

from searchWikipedia import getWikipediaLink
from searchGoogleimage import doImageSearch

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/input", methods=['POST'])
def input():
    originData = request.get_json(silent=True)['content']

    result = {}
    result['originContent'] = originData
    result['generatedData'] = getWikipediaLink(originData)

    print result
    return jsonify(result)


if __name__ == '__main__':
    app.debug = True
    app.run()
