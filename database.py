from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData
#from sqlalchemy.sql import select

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

    def __init__(self):
        self.db_engine = create_engine(self.db_name, echo=True)
        self.conn = self.db_engine.connect()
        metadata.create_all(self.db_engine)

    def save(self, name, date, headline, intro):
        try:
            #trans = self.conn.begin()
            result = self.conn.execute(
                self.news_table.insert().values(name=name,date=date,headline=headline,intro=intro)
            )
            #trans.commit()
        except Exception as e:
            print(e)
    
    def getAll(self):
        s = self.news_table.select()
        result = self.conn.execute(s)
        return [dict(row) for row in result]

NewsDB = NewsDatabaseClass()