import csv
from bs4 import BeautifulSoup, Tag
import requests

NEWS = "news"
URL = "url"
CLASS_OVERLAP = "classOverlap"
CLASS_HEADLINE = "classHeadline"
CLASS_INTRO = "classIntro"

def retrieve_newslist():
    result = []
    csvFile = open('newsList.csv')
    for row in csv.DictReader(csvFile):
        result.append(row)
    return result

def scrape_news(news :dict):
    page = requests.get(news[URL])
    soup = BeautifulSoup(page.content, 'html.parser')
    overlap = soup.select('.' + news[CLASS_OVERLAP])
    res = []
    for element in overlap:
        temp = {}
        headline = element.select_one('.' + news[CLASS_HEADLINE])
        intro = element.select_one('.' + news[CLASS_INTRO])
        temp = fillup_dictionary(temp, "headline",headline)
        temp = fillup_dictionary(temp, "intro",intro)
        res.append(temp)

    return res

def fillup_dictionary(ele: dict, name, tag: Tag):
    if isinstance(tag, type(None)) == False:
        ele[name] = tag.contents[0]
    else:
        ele[name] = ""
    return ele