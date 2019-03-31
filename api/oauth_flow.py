from flask import Blueprint, Flask, request
from databases import db
import os
import pprint

from slackclient import SlackClient


oauth = Blueprint("oauth", __name__, url_prefix="/oauth")

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
oauth_scope = os.environ.get("SCOPE")


@oauth.route("/begin_auth", methods=["GET"])
def pre_install():
    return f'<a href="https://slack.com/oauth/authorize?scope={oauth_scope}&client_id={client_id}">Add to Slack</a>'


@oauth.route("/finish_auth", methods=["GET", "POST"])
def post_install():
    auth_code = request.args["code"]
    sc = SlackClient("")

    auth_response = sc.api_call(
        "oauth.access", client_id=client_id, client_secret=client_secret, code=auth_code
    )
    resp = {
        "user_token": auth_response["access_token"],
        "bot_token": auth_response["bot"]["bot_access_token"],
        "bot_user_id": auth_response["bot"]["bot_user_id"],
        "team_id": auth_response["team_id"],
        "installing_user": auth_response["user_id"],
    }

    pprint.pprint(resp)
    return "Auth completed"
