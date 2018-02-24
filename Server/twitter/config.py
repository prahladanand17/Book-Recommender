import os

class Config(object):
    APP_NAME = 'Book-Recommender'
    CONSUMER_KEY = os.getenv('CONSUMER_KEY', '').strip()
    CONSUMER_SECRET = os.getenv('CONSUMER_SECRET', '').strip()
    SECRET_KEY = "Some Random String"
    EMBEDDING_DIM = 250
    CONTEXT_SIZE = 3

