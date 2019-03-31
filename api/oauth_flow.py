from flask import Blueprint, Flask, request
from databases import db
import os
import pprint

from slackclient import SlackClient


oauth = Blueprint("oauth", __name__, url_prefix="/oauth")

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
oauth_scope = os.environ.get("SCOPE")


class Install_response:
    def success_install(self, **kwargs):
        resp = {
            "user_token": kwargs["user_token"],
            "bot_token": kwargs["bot_token"],
            "bot_user_id": kwargs["bot_user_id"],
            "team_id": kwargs["team_id"],
            "installing_user": kwargs["installing_user"],
        }
        return resp


@oauth.route("/finish_auth", methods=["GET", "POST"])
def post_install():
    auth_code = request.args["code"]
    sc = SlackClient("")

    auth_response = sc.api_call(
        "oauth.access", client_id=client_id, client_secret=client_secret, code=auth_code
    )

    print(
        Install_response().success_install(
            user_token=auth_response["access_token"],
            bot_token=auth_response["bot"]["bot_access_token"],
            bot_user_id=auth_response["bot"]["bot_user_id"],
            team_id=auth_response["team_id"],
            installing_user=auth_response["user_id"],
        )
    )

    return "Auth completed"
