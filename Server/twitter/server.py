import os;
import tweepy;
from flask import Flask;
from Server.twitter.routes.root import loginBluePrint
from Server.twitter.routes.home import homeBlueprint

def create_app():
    app = Flask(__name__, template_folder='../../templates', static_folder='../../static')
    app.register_blueprint(loginBluePrint)
    app.register_blueprint(homeBlueprint)

    from Server.twitter.config import Config
    app.config.from_object(Config)


    return app




app = create_app()