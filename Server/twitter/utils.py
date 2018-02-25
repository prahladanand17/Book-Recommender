def combine(my_tweets, retweets):
    tweets = []
    for key in my_tweets:
        tweets.append(key)
    for key in retweets:
        tweets.append(key)
    return tweets

def contains_numbers(s):
    return any(char.isdigit() for char in s)

def get_user_text(tweets):
    text = ""
    for key in tweets:
        text += key.full_text + " "
    return text

def contains_numbers(s):
    for char in s:
        return any(char.isdigit)

def clean_text(words):
    for i in range(words):
        if contains_numbers(words[i]):
            words.pop(words[i])
    return words

