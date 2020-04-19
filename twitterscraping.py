from twitterscraper import query_tweets
import datetime as dt
import pandas as pd

begin_date = dt.date(2020, 1, 1)
end_date = dt.date(2020, 4, 1)
limit = 1500
lang = 'spanish'

tweets = query_tweets(["panama", "coronavirus"], begindate=begin_date,
                      enddate=end_date, limit=limit, lang=lang)

df = pd.DataFrame(t.__dict__ for t in tweets)
df.sort_values("timestamp", ascending = True, inplace=True)
df.drop_duplicates("tweet_id", inplace=True)
df.to_csv('twitter_data.csv', index=False)
