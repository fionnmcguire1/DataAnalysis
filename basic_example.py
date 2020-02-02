


from twitterscraper import query_tweets
import datetime as dt
import pandas as pd
import json



begin_date = dt.date.today()
end_date = begin_date + dt.timedelta(days=1)
data_folder = "JSONDataFiles/"


limit = 1000
lang = 'english'


tweets = query_tweets('#sixnations', begindate = begin_date, enddate = end_date, limit = limit, lang = lang)

#print(tweets[0].keys())
list_of_json_tweets = []
for tweet in tweets:
        tweet_time = tweet.timestamp
        tweet.timestamp = tweet_time.strftime('%Y-%m-%d %H:%M:%S')

        list_of_json_tweets.append(vars(tweet))
        print(tweet.text)

#df = pd.DataFrame(t._dict_ for t in tweets)
str_date = begin_date.strftime("%Y-%m-%d")
jsonfile = open(data_folder+str_date+".json","w")
for item in list_of_json_tweets:
    json.dump(item,jsonfile)
jsonfile.close()
