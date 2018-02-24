import os;
import tweepy;
from flask import Flask;
from Server.twitter.routes.root import loginBluePrint
from Server.twitter.routes.home import homeBlueprint

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='style')
    app.register_blueprint(loginBluePrint)
    app.register_blueprint(homeBlueprint)
    return app

app = create_app()