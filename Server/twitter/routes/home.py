from Server.twitter.routes.login import *
from Server.twitter.utils import *
from Server.Recommender.model.utils import *
from Server.Recommender.model.model import *

homeBlueprint = Blueprint('home', __name__)


@homeBlueprint.route("/", methods=['GET'])
def home():
    """
    Handles route '/'. If the user has not logged-in redirect to the login
    page. Otherwise render the 'home' page template.
    """
    access_token = session.get('access_token', None)

    if not access_token:
        # access_token not in session. Redirect to login page.
        return redirect(url_for('login.login'))

    # Found an access_token in session. Render the home page.
    access_token_secret = session.get('access_token_secret')
    config = current_app.config

    consumer_key = config['CONSUMER_KEY']
    consumer_secret = config['CONSUMER_SECRET']
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)


    my_tweets = api.user_timeline(tweet_mode = "extended", retweeted = "false")
    retweets = api.retweets_of_me(tweet_mode = "extended", )
    tweets = combine(my_tweets, retweets)
    raw_text = get_user_text(tweets)
    raw_text = raw_text.lower()

    word_to_ix = {}
    ix_to_word = {}


    words = raw_text.split()
    text = clean_text(words)



    vocab = set(text)
    vocab_size = len(text)

    for i, word in enumerate(vocab):
        word_to_ix[word] = i
        ix_to_word[i] = word

    context_data, context, target = get_context_data(text)


    model = CBOW(vocab_size, config['EMBEDDING_DIM'])
    loss_function = nn.NLLLoss()
    gd_optimizer = torch.optim.Adagrad(model.parameters(), lr = 0.001)

    train(model, context_data, loss_function, gd_optimizer, 50, context, target, word_to_ix)





    return render_template("home.jinja2", APP_NAME=config['APP_NAME'])