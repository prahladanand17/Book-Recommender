def combine(my_tweets, retweets):
    tweets = []
    for key in my_tweets:
        tweets.append(key)
    for key in retweets:
        tweets.append(key)
    return tweets

def get_user_text(tweets):
    text = ""
    for key in tweets:
        text += key.full_text + " "
    return text
