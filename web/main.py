from flask import Blueprint, Flask
import os

web = Blueprint('web', __name__,)


@web.route('/')
def index():
    return "Index Page"


@web.route('/install')
def add_to_slack_install_page():
    client_id = os.environ.get('CLIENT_ID')
    client_secret = os.environ.get('CLIENT_SECRET')
    return "Successfully removed Subscription"