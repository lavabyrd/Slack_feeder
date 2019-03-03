from flask import Blueprint, Flask


api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/add_feed', methods=['POST'])
def add_rss_feed_subscription():
    return "Successfully added"

@api.route('/remove_feed', methods=['POST'])
def remove_rss_feed_subscription():
    return "Successfully removed Subscription"