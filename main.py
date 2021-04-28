from datetime import datetime
from webscraper import retrieve_newslist, scrape_news, NEWS
from server import app;
from database import NewsDB
from threading import Event, Thread

def run_and_save():
    newsList = retrieve_newslist()
    for news in newsList:
        print(news[NEWS])
        scraped = scrape_news(news)
        for single in scraped:
            if len(single["intro"]) == 0:
                single["intro"] = "-"
            single["headline"] = single["headline"].replace("\n","")
            single["intro"] = single["intro"].strip().replace("\n","")
            if len(single["intro"] ) > 250:
                single["intro"] = single["intro"][:249]
            print(single)
            NewsDB.save(
                news[NEWS],
                datetime.now().strftime("%d/%m/%Y"),
                single["headline"],
                single["intro"],
            )

def call_repeatedly(interval, func, *args):
    stopped = Event()
    def loop():
        func(*args)
        while not stopped.wait(interval): # the first call is in `interval` secs
            func(*args)
    Thread(target=loop).start()    
    return stopped.set

def main():
    # 7 days interval
    call_repeatedly(60 * 60 * 24 * 7, run_and_save)
    app.run()
    
if __name__ == "__main__":
    main()
