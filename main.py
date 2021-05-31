from datetime import datetime

from components.webscraper import retrieve_newslist, scrape_news, NEWS
from components.trends import get_trends
from components.database import NewsDB

from apscheduler.schedulers.background import BackgroundScheduler

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
    
def call_at_six(func, *args):
    sched = BackgroundScheduler(daemon=True)
    sched.add_job(
        lambda: func(*args), 
        'cron', 
        hour = '6, 18'
    )
    sched.start()

def call_at_zero(func, *args):
    sched = BackgroundScheduler(daemon=True)
    sched.add_job(
        lambda:func(*args), 
        'cron', 
        hour = '0'
    )
    sched.start()

#
# MAIN
#
def main():

    call_at_six(run_and_save_news)
    call_at_zero(run_and_save_trends)

    app.run(host= '0.0.0.0')
    
if __name__ == "__main__":
    main()