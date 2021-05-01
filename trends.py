import pandas as pd
from pytrends.request import TrendReq

def get_trends():
    pytrends = TrendReq(hl="de-DE",tz = 200, geo="de")
    df = pytrends.trending_searches(pn="germany")
    return df.values