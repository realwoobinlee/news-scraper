from webscraper import retrieve_newslist, scrape_news, NEWS

def main():
    # 1. 
    newsList = retrieve_newslist()
    for news in newsList:
        print(news[NEWS])
        scraped = scrape_news(news)
        print(scraped)
    # 2. 
    
if __name__ == "__main__":
    main()
