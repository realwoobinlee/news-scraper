import json
from flask import Flask
from datetime import datetime
from components.database import NewsDB

app = Flask(__name__)

@app.route('/data/news/all')
def get_all_data():
    res = NewsDB.get_all_news()
    return json.dumps({"value": res}, ensure_ascii=False)

@app.route('/data/trends/all')
def get_all_trends():
    res = NewsDB.get_all_trends()
    return json.dumps({"value": res}, ensure_ascii=False)

@app.route('/test')
def get_test():
    return json.dumps({"value": "test"}, ensure_ascii=False)