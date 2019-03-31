from flask import Blueprint, Flask
import os
from databases import db

web = Blueprint("web", __name__)

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
oauth_scope = os.environ.get("SCOPE")


@web.route("/")
@web.route("/begin_auth")
def pre_install():
    return f'<a href="https://slack.com/oauth/authorize?scope={oauth_scope}&client_id={client_id}">Add to Slack</a>'
