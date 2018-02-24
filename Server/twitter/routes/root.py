from flask import Blueprint, current_app, request, redirect, url_for, session
import tweepy
from flask import render_template

loginBluePrint = Blueprint('auth', __name__)


@loginBluePrint.route('/login', methods=['GET'])
def login():
    """
    Render a login template with 'Login using Facebook' button for the
    user to login.
    """

    # Show the login page.
    config = current_app.config
    return render_template("login.jinja2", APP_NAME=config['APP_NAME'])


@loginBluePrint.route('/logout')
def logout():
    """
    Need to logout the user. Logging out of this app doesn't necessarily have
    to logout of facebook. So all you have to do is just clear the user session.
    """
    session.clear()

    # user has been logged-out. But need to render a view. So re-direct the
    # user back to login page.
    return redirect(url_for('root.login'))


@loginBluePrint.route('/login', methods=['POST'])
def authenticate():
    """
    Called when the user clicked on the 'Login with Twitter' button in the
    login page. Authenticate with twitter.
    """

    config = current_app.config

    # The consumer keys can be found on your application's Details
    # page located at https://dev.twitter.com/apps (under "OAuth settings")
    consumer_key = config['TWITTER_CONSUMER_KEY']
    consumer_secret = config['TWITTER_CONSUMER_SECRET']

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret,
                               url_for('root.authenticated',
                                       _external=True))
    redirect_url = auth.get_authorization_url(signin_with_twitter=True)

    # In a web application we will be using a callback request. So we must
    # store the request token in the session since we will need it inside the
    # callback URL request.
    session['request_token'] = auth.request_token

    # redirect the user to twitter auth endpoint.
    return redirect(redirect_url)


@loginBluePrint.route('/login/authenticated')
def authenticated():
    """
    Twitter auth callback. Will be redirected here after login completes.
    """

    # This function will be called when twitter login is succcessful.
    # Confirm the identity of the person logged in.
    # https://developers.facebook.com/docs/facebook-login/manually-build-a-login-flow#confirm
    config = current_app.config
    oauth_token = request.args.get('oauth_token')
    verifier = request.args.get('oauth_verifier')

    # Get the access token using the verifier token.
    if oauth_token and verifier:
        consumer_key = config['TWITTER_CONSUMER_KEY']
        consumer_secret = config['TWITTER_CONSUMER_SECRET']
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret,
                                   url_for('root.authenticated',
                                           _external=True))
        auth.request_token = session['request_token']

        [access_token, access_token_secret] = auth.get_access_token(verifier)
        if access_token and access_token_secret:
            session['access_token'] = access_token
            session['access_token_secret'] = access_token_secret

            # Fetch the user info
            api = tweepy.API(auth)
            profile = api.me()

            # If a valid user has been fetched, store in the session.
            if profile:
                session['user'] = {
                    'id': getattr(profile, 'id', None),
                    'fullName': getattr(profile, 'name', None),
                    'email': getattr(profile, 'email', None),
                    'firstName': getattr(profile, 'first_name', None),
                    'lastName': getattr(profile, 'last_name', None),
                    'profileLink': getattr(profile, 'link', None),
                    'profileImageUrl': getattr(profile, 'profile_image_url',
                                               None)
                }
            else:
                session['user'] = None

            # Successfully logged. Redirect to the main page.
            return redirect(url_for('home.home'))

    # User cancelled login or failed to get and verify the access token.
    # redirect back to login page.
    # TODO: Figure out the best way to set some error message to be shown in
    # the login apge.
    return redirect(url_for('root.login'))