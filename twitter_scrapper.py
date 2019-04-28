import GetOldTweets3 as got


tweetCriteria = got.manager.TweetCriteria().setQuerySearch('infosys')\
                                           .setSince("2018-01-01")\
                                           .setUntil("2018-01-02")
                                        #    .setMaxTweets(100)

for tweet in got.manager.TweetManager.getTweets(tweetCriteria):
    print(tweet.text, tweet.date)
