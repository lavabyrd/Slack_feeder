from flask import Blueprint, json, Flask, request
import db
from SlackFeedr import parse

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/add_feed', methods=['POST'])
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
            # return parse.test_feed(feed_url)
            print("passed the feed test")
            return parse.test_rss_feed(feed_url)
            # return db.insert_feed_url_to_db(payload)           
    except:
        return "sorry, you've experienced an error"


@api.route('/remove_feed', methods=['POST'])
def remove_rss_feed_subscription():
    return "removed feed"
