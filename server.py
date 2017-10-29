from flask import Flask
from flask import request
from flask import jsonify
import re
import json
import time
from flask_cors import CORS


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from workflow import generateContent
from db import db_connect, db_counterup, db_counterdown

app = Flask(__name__)
CORS(app)
db_connect()

@app.route("/")
def ping():
    return "OK"

@app.route("/input", methods=['POST'])
def input():
    # FOR LIVE PRESENTATION
    # time.sleep( 5 )
    # with open('mockResponse.json') as json_data:
    #     return jsonify(json.load(json_data))

    content =  request.get_json(silent=True)['content']    
    # content = re.sub('[^a-zA-Z. 0-9]', '', content)
    originalContent = content
    print "------------------"
    print originalContent
    print "------------------"
    result = generateContent(originalContent)
    print result
    return jsonify(result)


@app.route("/feedback", methods=['POST'])
def feedback():
    fb = request.get_json(silent=True)
    cat = get_topic(fb['category'])
    mt = fb['mediatype']
    db_counterup(cat, mt)
    return "OK"


def get_topic(text):
    return text.split('/')[1]

if __name__ == '__main__':
    app.debug = True
    app.run(host= '0.0.0.0')
