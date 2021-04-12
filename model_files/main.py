import tweepy
from textblob import TextBlob
import pandas as pd
import numpy as np
import re

#Twitter API credentials
consumerKey = 'LpJVXy1gObYUOmT3XLHDTN5hd'
consumerSecret = 'WWAPAxlNjLwT3E0ONPK1IVxH7oOBgdt8PUxJBNgPMABk3rrQYn'
accessToken = '798155043417559040-y7enZ8zyMoypIhwvIJc8LR5fH6KP61S'
accessTokenSecret = 'ZwgARdPWcuHFGEfnt57v9eVTIZaBRWLPHhcQvhlNB791l'

# create the authentication object
authenticate = tweepy.OAuthHandler(consumerKey, consumerSecret)
# set the access token and access token secret
authenticate.set_access_token(accessToken, accessTokenSecret)
# create the API object while passing in the auth information
api = tweepy.API(authenticate, wait_on_rate_limit = True)

def getTrends():
  try:
    woeid = 23424848
    trends_result = api.trends_place(woeid)
    trends_list = []

    for trend in trends_result[0]["trends"][:10]:
      trends_list.append(trend["name"])

  except tweepy.error.TweepError:
    print("There are no trending topics for that location")
  return trends_list



def cleanText(text):
  text = re.sub(r'@[A-Za-z0-9]+','', text) # Removed @mentions
  text = re.sub(r'#','', text) # Removed hashtag symbol
  text = re.sub(r'RT[\s]+', '', text) #Removed 'RT'
  text = re.sub(r'https?:\/\/\S+', '', text) # Removed the hyper links
  regrex_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
  text = regrex_pattern.sub(r'',text)
  return text



def getPolarity(text):
  return TextBlob(text).sentiment.polarity



def getTweets():
  t = getTrends()
  n=25
  df=pd.DataFrame(index=np.arange(n), columns=np.arange(10))
  for i in range(0, 10):
    tweets = tweepy.Cursor(api.search, q=t[i], lang="en", tweet_mode='extended').items(n)
    list_tweets = [tweet for tweet in tweets]
    df[i] = list_tweets

    c=0
    for tweet in df[i]:
      try:
        text = tweet.retweeted_status.full_text
      except AttributeError:
        text = tweet.full_text
      df.iloc[c][i] = text
      c=c+1
  return df



def getSentiments():
  arr = np.zeros((10, 3))
  df = getTweets()
  n=25
  pdf = pd.DataFrame(index=np.arange(n), columns=np.arange(1))
  for i in range(0, 10):
    df[i]=df[i].apply(cleanText)
    pdf[0]=df[i].apply(getPolarity)

    pos=0
    neg=0
    neu=0

    for j in pdf[0]:
      if j>0:
        pos=pos+1
      elif j==0:
        neu=neu+1
      else:
        neg=neg+1

    arr[i, 0] = pos*4
    arr[i, 1] = neg*4
    arr[i, 2] = neu*4
  return arr
