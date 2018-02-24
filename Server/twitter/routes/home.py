from flask import Blueprint, render_template, current_app, session, redirect, \
    url_for

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
        return redirect(url_for('root.login'))

    # Found an access_token in session. Render the home page.
    config = current_app.config
    return render_template("home.jinja2", APP_NAME=config['APP_NAME'])