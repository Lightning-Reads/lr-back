from flask import Flask
from flask import request
from flask import jsonify


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from workflow import generateContent
from db import db_connect, db_counterup, db_counterdown

app = Flask(__name__)
db_connect()

@app.route("/")
def ping():
    return "OK"

@app.route("/input", methods=['POST'])
def input():
    originalContent = request.get_json(silent=True)['content']
    result = generateContent(originalContent)
    print result
    return jsonify(result)


@app.route("/feedback", methods=['POST'])
def feedback():
    fb = request.get_json(silent=True)
    db_counterup(fb['category'], fb['mediatype'])
    return "OK"
    

if __name__ == '__main__':
    app.debug = True
    app.run(host= '0.0.0.0')
