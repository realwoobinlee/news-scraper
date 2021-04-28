import json
from flask import Flask
from datetime import datetime
from webscraper import retrieve_newslist, scrape_news, NEWS
from database import NewsDB

app = Flask(__name__)

@app.route('/data/all')
def get_all_data():
    res = NewsDB.getAll()
    print(res)
    return json.dumps({"value": res})

#TODO: Imple
@app.route('/data/query')
def getQueriedData():
    return json.dumps({'name': 'alice',
                       'email': 'alice@outlook.com'})
