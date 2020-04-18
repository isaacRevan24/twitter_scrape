from twitterscraper import query_tweets
import datetime as dt
import pandas as pd

begin_date = dt.date(2019, 12, 1)
end_date = dt.date(2020, 4, 1)
limit = 1000
lang = 'spanish'

tweets = query_tweets("covid-19", begindate=begin_date,
                      enddate=end_date, limit=limit, lang=lang)

df = pd.DataFrame(t.__dict__ for t in tweets)
df.to_csv('datosTest.csv', index=False)
