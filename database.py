from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData

metadata = MetaData()

class NewsDatabaseClass:
    # Database Variable
    db_name = 'postgresql://postgres:!MyProject_15TZjc+!@localhost:5432/news'
    
    # DB Connection
    db_engine = None
    conn = None
    
    news_table = Table("news", metadata,
        Column("name", String),
        Column("date", String),
        Column("headline", String, primary_key=True),
        Column("intro", String),
    )

    trends_table = Table("trends", metadata,
        Column("date", String, primary_key=True),
        Column("keyword", String, primary_key=True),
    )

    def __init__(self):
        self.db_engine = create_engine(self.db_name, echo=True)
        self.conn = self.db_engine.connect()
        metadata.create_all(self.db_engine)

    def save_news(self, name, date, headline, intro):
        try:
            result = self.conn.execute(
                self.news_table.insert().values(name=name,date=date,headline=headline,intro=intro)
            )
        except Exception as e:
            print(e)
    
    def get_all_news(self):
        s = self.news_table.select()
        result = self.conn.execute(s)
        return [dict(row) for row in result]

    def save_trends(self, date, keyword):
        try:
            result = self.conn.execute(
                self.trends_table.insert().values(date=date,keyword=keyword)
            )
        except Exception as e:
            print(e)

    def get_all_trends(self):
        s = self.trends_table.select()
        result = self.conn.execute(s)
        return [dict(row) for row in result]

NewsDB = NewsDatabaseClass()