import tweepy

consumer_key = "rvWwzm1kDXiJ2UUFP7Sgfsj6q"
consumer_secret = "YdxOZiaaOCH5vzlqrOpBKDhIYn3f4hQFhQ8hwDjL2nGcHe26XJ"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

lyric = '\"I\'m the killer on the evening news.\"'
lyric += " - Rozz Dyliams"



api.update_status(lyric)
