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
    for char in s:
        return any(char.isdigit)

def clean_text(words):
    text = []
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)
    for i in len(words):
        if not contains_numbers(words[i]):
            text.append(emoji_pattern.sub(r'', words[i]))

    return text

