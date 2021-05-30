from datetime import datetime
from threading import Event, Thread

from components.webscraper import retrieve_newslist, scrape_news, NEWS
from components.trends import get_trends
from components.database import NewsDB

from controller.server import app;

def run_and_save_news():
    news_list = retrieve_newslist()
    for news in news_list:
        print(news[NEWS])
        scraped = scrape_news(news)
        for single in scraped:
            if len(single["intro"]) == 0:
                single["intro"] = "-"
            single["headline"] = single["headline"].replace("\n","")
            single["intro"] = single["intro"].strip().replace("\n","")
            NewsDB.save_news(
                news[NEWS],
                datetime.now().strftime("%d/%m/%Y"),
                single["headline"],
                single["intro"],
            )

def run_and_save_trends():
    list_trends = get_trends()
    for trends in list_trends:
        NewsDB.save_trends(
            datetime.now().strftime("%d/%m/%Y"),
            trends[0]
        )

def call_repeatedly(interval, func, *args):
    stopped = Event()
    def loop():
        func(*args)
        while not stopped.wait(interval): # the first call is in `interval` secs
            func(*args)
    Thread(target=loop).start()    
    return stopped.set

#
# MAIN
#
def main():
    # 7 days interval
    call_repeatedly(60 * 60 * 24 / 2, run_and_save_news)
    call_repeatedly(60 * 60 * 1, run_and_save_trends)
    app.run(host= '0.0.0.0')
    
if __name__ == "__main__":
    main()
