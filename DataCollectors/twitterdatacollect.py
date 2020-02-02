class TwitterDataCollect(object):

    def __init__(self):
        self.markers = []
        self.language = 'english'
        self.start_time = None
        self.end_time = None
        self.destination = "JSONDataFiles/"

    def buildMarkers(self,markers):

        for mark in markers:
            self.markers.append(str(mark))
            self.markers.append("#"+str(mark))


    def buildTimeFrame(self,mode,custom_start=None,custom_end=None):

        #Mode 1 -> One Day Rush
        # Get all from today
        if mode == 1:
            self.start_time  

        #Mode 2 -> XI
        #Data From the last 15 minutes

        #Mode 3
        #Data From the last week

        #Mode 4
        #Data from the last month

        #Mode 5
        #Data from the last year

    def setLimit(limit=1000)

    def setLang(lang='english')

    def collectData()
    from twitterscraper import query_tweets
    import datetime as dt
    import pandas as pd
    import json

    #Build a class to call a custom scrap or to perform a default scrape
    #This will require methods which have certain default hash tags


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

    #df = pd.DataFrame(t._dict_ for t in tweets)
    str_date = begin_date.strftime("%Y-%m-%d")
    jsonfile = open(data_folder+str_date+".json","w")
    length_of_tweet_list = len(list_of_json_tweets)
    for index,item in enumerate(list_of_json_tweets):
        json.dump(item,jsonfile)
        if length_of_tweet_list-1 != index:
            jsonfile.write(",")

    jsonfile.close()
