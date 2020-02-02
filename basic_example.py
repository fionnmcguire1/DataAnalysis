


from twitterscraper import query_tweets
import datetime as dt
import pandas as pd


begin_date = dt.date(2019,4,15)
end_date = dt.date(2019,4,18)


limit = 5
lang = 'english'


tweets = query_tweets('notre dame fire', begindate = begin_date, enddate = end_date, limit = limit, lang = lang)
df = pd.DataFrame(t._dict_ for t in tweets)
