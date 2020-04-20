from twitterscraper import query_tweets
import datetime as dt
import pandas as pd

# Configuración de query
begin_date = dt.date(2020, 1, 1)
end_date = dt.date.today()
limit = 1000000
lang = 'spanish'
lugares = ("bocas del toro", "chiriqui", "cocle", "colon", "Darien", "herrera", "los santos", "panama", "panama oeste", "veraguas", "san miguelito", "arraijan", "chorrera", "david", "veracruz", "aguadulce", "los santos", "juan dias")

# Busqueda "#coronavirus"
for lugar in lugares:
    tweets = query_tweets([lugar ,"coronavirus"], begindate=begin_date, enddate=end_date, limit=limit, lang=lang)
    df = pd.DataFrame(t.__dict__ for t in tweets)
    df.sort_values("timestamp", ascending = True, inplace=True)
    df.drop_duplicates("tweet_id", inplace=True)
    nombre_archivo = "tweet_dataset_1_"+lugar.replace(" ", "")+".csv"
    df.to_csv(nombre_archivo, index=False)


# Busqueda "#covid-19"
for lugar in lugares:
    tweets = query_tweets([lugar ,"covid-19"], begindate=begin_date, enddate=end_date, limit=limit, lang=lang)
    df = pd.DataFrame(t.__dict__ for t in tweets)
    df.sort_values("timestamp", ascending = True, inplace=True)
    df.drop_duplicates("tweet_id", inplace=True)
    nombre_archivo = "tweet_dataset_2_"+lugar.replace(" ", "")+".csv"
    df.to_csv(nombre_archivo, index=False)



# Busqueda "#coronavirus"
for lugar in lugares:
    tweets = query_tweets([lugar ,"pandemia"], begindate=begin_date, enddate=end_date, limit=limit, lang=lang)
    df = pd.DataFrame(t.__dict__ for t in tweets)
    df.sort_values("timestamp", ascending = True, inplace=True)
    df.drop_duplicates("tweet_id", inplace=True)
    nombre_archivo = "tweet_dataset_3_"+lugar.replace(" ", "")+".csv"
    df.to_csv(nombre_archivo, index=False)
