from twitterscraper import query_tweets
import datetime as dt
import pandas as pd

# Configuración de query
begin_date = dt.date(2020, 1, 1)
end_date = dt.date.today()
limit = 1000000
lang = 'spanish'
lugares = ("bocas del toro", "chiriqui", "cocle", "colon", "Darien", "herrera", "los santos", "panama", "panama oeste",
           "veraguas", "san miguelito", "arraijan", "chorrera", "david", "veracruz", "aguadulce", "los santos", "juan diaz")

psi = ("tristeza", "llanto", "decaimiento", "desanimo", "desmotivacion", "desesperanza",
       "cansancio", "sin animo", "desinteres", "desconcentración", "debilidad", "perdida de apetito")


# Busqueda "#coronavirus"
for lugar in lugares:
    for ps in psi:
        tweets = query_tweets([lugar, ps, "coronavirus"], begindate=begin_date,
                              enddate=end_date, limit=limit, lang=lang)
        df = pd.DataFrame(t.__dict__ for t in tweets)
        if df.empty:
            pass
        else:
            df.sort_values("timestamp", ascending=True, inplace=True)
            df.drop_duplicates("tweet_id", inplace=True)
            nombre_archivo = "tweet_dataset_1_" + \
                lugar.replace(" ", "")+"_"+ps.replace(" ", "")+".csv"
            df.to_csv(nombre_archivo, index=False, encoding="utf-8")


# Busqueda "#covid"
for lugar in lugares:
    for ps in psi:
        tweets = query_tweets([lugar, ps, "covid"], begindate=begin_date,
                              enddate=end_date, limit=limit, lang=lang)
        df = pd.DataFrame(t.__dict__ for t in tweets)
        if df.empty:
            pass
        else:
            df.sort_values("timestamp", ascending=True, inplace=True)
            df.drop_duplicates("tweet_id", inplace=True)
            nombre_archivo = "tweet_dataset_2_" + \
                lugar.replace(" ", "")+"_"+ps.replace(" ", "")+".csv"
            df.to_csv(nombre_archivo, index=False, encoding="utf-8")


# Busqueda "#pandemia"
for lugar in lugares:
    for ps in psi:
        tweets = query_tweets([lugar, ps, "pandemia"], begindate=begin_date,
                              enddate=end_date, limit=limit, lang=lang)
        df = pd.DataFrame(t.__dict__ for t in tweets)
        if df.empty:
            pass
        else:
            df.sort_values("timestamp", ascending=True, inplace=True)
            df.drop_duplicates("tweet_id", inplace=True)
            nombre_archivo = "tweet_dataset_3_" + \
                lugar.replace(" ", "")+"_"+ps.replace(" ", "")+".csv"
            df.to_csv(nombre_archivo, index=False, encoding="utf-8")
