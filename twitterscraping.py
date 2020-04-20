from twitterscraper import query_tweets
import datetime as dt
import pandas as pd

begin_date = dt.date(2020, 1, 1)
end_date = dt.date(2020, 4, 1)
limit = 1000000
lang = 'spanish'

# Busqueda "#coronavirus"
tweets = query_tweets(["panama", "coronavirus"], begindate=begin_date,
                      enddate=end_date, limit=limit, lang=lang)

df = pd.DataFrame(t.__dict__ for t in tweets)
df.sort_values("timestamp", ascending = True, inplace=True)
df.drop_duplicates("tweet_id", inplace=True)
df.to_csv('twitter_dataset_1.csv', index=False)


# Busqueda "#covid-19"
tweets = query_tweets(["panama", "covid-19"], begindate=begin_date,
                      enddate=end_date, limit=limit, lang=lang)

df = pd.DataFrame(t.__dict__ for t in tweets)
df.sort_values("timestamp", ascending = True, inplace=True)
df.drop_duplicates("tweet_id", inplace=True)
df.to_csv('twitter_dataset_2.csv', index=False)



# Busqueda "#pandemia"
tweets = query_tweets(["panama", "pandemia"], begindate=begin_date,
                      enddate=end_date, limit=limit, lang=lang)

df = pd.DataFrame(t.__dict__ for t in tweets)
df.sort_values("timestamp", ascending = True, inplace=True)
df.drop_duplicates("tweet_id", inplace=True)
df.to_csv('twitter_dataset_3.csv', index=False)





