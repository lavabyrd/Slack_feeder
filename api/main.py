from flask import Blueprint, json, Flask, request
import db, os
from SlackFeedr import parse
from slackclient import SlackClient
from blocks_builds import block
import pprint

api = Blueprint("api", __name__, url_prefix="/api")

sc = SlackClient(os.environ.get("BOT_TOKEN"))


@api.route("/add_feed", methods=["POST"])
def add_rss_feed_subscription():
    """Add feed endpoint
    Returns:
        [string] -- [confirmation of RSS Feed]
    Expects:
        token=gIkuvaNzQIHg97ATvDxqgjtO
        &team_id=T0001
        &team_domain=example
        &enterprise_id=E0001
        &enterprise_name=Globular%20Construct%20Inc
        &channel_id=C2147483705
        &channel_name=test
        &user_id=U2147483697
        &user_name=Steve
        &command=/weather
        &text=94070
        &response_url=https://hooks.slack.com/commands/1234/5678
        &trigger_id=13345224609.738474920.8088930838d88f008e0
    Information:
        https://api.slack.com/slash-commands
    """
    try:
        payload = request.form.to_dict()
        feed_url = payload["text"]
        # response_url = payload["response_url"]
        if not feed_url:
            return "please enter some text e.g. `/add_feed test.com`"
        else:
            if parse.test_rss_feed(feed_url) is True:
                sc.api_call(
                    "chat.postMessage",
                    channel=payload["channel_id"],
                    text="hi",
                    blocks=block.success_block,
                )
                return ""
            else:
                return f"{feed_url} is not a valid RSS feed. Please see <https://rss.com/rss-feed-validators/|this link> for some feed validators"

            # return db.insert_feed_url_to_db(payload)
    except:
        return "sorry, you've experienced an error"


@api.route("/remove_feed", methods=["POST"])
def remove_rss_feed_subscription():
    return "removed feed"


@api.route("/actions", methods=["POST"])
def action_route():
    payload = json.loads(request.form.get("payload"))
    for a in payload["actions"]:
        if a["block_id"] == "add_decline":
            if a["selected_option"]["value"] == "add_rss_feed":
                return "that worked"
            elif a["selected_option"]["value"] == "cancel":
                return "cancelled"
        # elif payload['callback_id'] == 'confirm_post':
        #     if payload['actions'][0]['name'] == 'cancelled_job':
        #         return payload["original_message"]["text"]
        #     elif payload['actions'][0]['name'] == 'PostJob':
        #         # sc.api_call("chat.postMessage",
        #         #             text=payload["original_message"]["text"],
        #         #             as_user="true",
        #         #             channel=target_channel)
        #         # sc.api_call('chat.update',
        #         #             ts=payload["message_ts"],
        #         #             channel=payload["channel"]["id"],
        #         #             as_user="true",
        #         #             text=payload["original_message"]["text"],
        #         #             attachments=responses.attachm_update)
        #         return ""
        #     else:
        #         return ""
        else:
            return "try again"
