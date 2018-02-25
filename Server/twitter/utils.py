import re
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

def contains_numbers(s):
    return any(char.isdigit() for char in s)

def clean_text(words):
    text = []
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)
    for w in words:
        if not contains_numbers(w):
            text.append(emoji_pattern.sub(r'', w))

    return text

