class TwitterDataCollect(object):

    def __init__(self):
        self.markers = []
        self.language = 'english'
        self.start_time = None
        self.end_time = None
        self.destination = "JSONDataFiles/"

    #Accepts list of string values as parameter
    def buildMarkers(self,markers=None):
        if isinstance(markers,list):
            for mark in markers:
                if isinstance(mark,str):
                    self.markers.append(str(mark))
                    if "#" not in mark:
                        self.markers.append("#"+str(mark))
                else: return False
        else: return False
        return True


    def buildTimeFrame(self,mode,custom_start=None,custom_end=None):
        import datetime as dt

        if custom_start is None:
            if mode == 1:
                #Mode 1 -> One Day Rush
                # Get all from today
                self.end_time = self.start_time + dt.timedelta(days=1)
                self.start_time = dt.datetime.today()


            elif mode == 2:
                #Mode 2 -> XI
                #Data From the last 15 minutes
                self.end_time =  dt.datetime.now()
                self.start_time = self.end_time - dt.timedelta(minutes=15)

            elif mode == 3:
                #Mode 3
                #Data From the last week
                self.end_time = dt.datetime.now()
                self.start_time = dt.end_time - dt.timedelta(days=7)

            elif mode == 4:
                #Mode 4
                #Data from the last month
                self.end_time = dt.datetime.now()
                self.start_time = dt.end_time - dt.timedelta(weeks=4)

            elif mode == 5:
                #Mode 5
                #Data from the last year
                self.end_time = dt.datetime.now()
                self.start_time = dt.end_time - dt.timedelta(weeks=52)
            else: return False

        else:
            #Assign custom start and end dates
            if 'datetime.datetime' in str(type(custom_start)) and 'datetime.datetime' in str(type(custom_end)):
                self.start_time = custom_start
                self.end_time = custom_end
            else: return False

        return True

    def setLimit(limit=1000):
        if isinstance(limit, int) and limit > 0:
            self.limit = limit
            return True
        else: return False

    def setLang(lang='english'):
        if isinstance(lang, str) and len(lang) > 0:
            self.lang = lang
            return True
        else: return False

    def collectData():
        from twitterscraper import query_tweets
        import datetime as dt
        import json

        #Build query string with all marker variations specified
        query_str = ""
        for marker in self.markers:
            query_str+=marker+" "

        #Collect data
        tweets = query_tweets(query_str,begindate=self.start_time,enddate=start.end_time,limit=self.limit,lang=self.lang)


        #Convert data into format that is jsonable
        list_of_json_tweets = []
        for tweet in tweets:
                tweet_time = tweet.timestamp
                tweet.timestamp = tweet_time.strftime('%Y-%m-%d %H:%M:%S')
                list_of_json_tweets.append(vars(tweet))

        #Write output
        file_name = self.start_time.strftime("%Y-%m-%d")
        jsonfile = open(self.destination+file_name+".json","w")
        length_of_tweet_list = len(list_of_json_tweets)
        length_of_tweet_list-=1
        for index,item in enumerate(list_of_json_tweets):
            json.dump(item,jsonfile)
            if length_of_tweet_list != index:
                json_file.write(",")

        json_file.close()
