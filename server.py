from flask import Flask
from flask import request
from flask import jsonify


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from workflow import generateContent

app = Flask(__name__)

@app.route("/")
def ping():
    return "OK"

@app.route("/input", methods=['POST'])
def input():
    originContent = request.get_json(silent=True)['content']
    result = generateContent(originContent)
    print result
    return jsonify(result)

if __name__ == '__main__':
    app.debug = True
    app.run()
