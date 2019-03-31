import os
from pymongo import MongoClient

#         feed_list.insert_one(
#             {
#                 "user_id": user_id,
#                 "feed_url": feed_url,
#                 "channel": channel,
#                 "workspace": workspace,
#                 "last_feed": latest,
#             }


class MongoRepository(object):
    def __init__(self):
        db_user = os.environ.get("DB_USER")
        db_pass = os.environ.get("DB_PASS")
        db_uri = os.environ.get("DB_URI")
        self.db = MongoClient(f"mongodb://{db_user}:{db_pass}@{db_uri}").get_database()

    def find_all(self, selector):
        return self.db.main_collection.find(selector)

    def find(self, selector):
        return self.db.main_collection.find_one(selector)

    def create(self, feed):
        return self.db.main_collection.insert_one(feed)

    def update(self, selector, feed):
        return self.db.main_collection.replace_one(selector, feed).modified_count

    def delete(self, selector):
        return self.db.main_collection.delete_one(selector).deleted_count

    def success_install(self, **kwargs):
        resp = {
            "user_token": kwargs["user_token"],
            "bot_token": kwargs["bot_token"],
            "bot_user_id": kwargs["bot_user_id"],
            "team_id": kwargs["team_id"],
            "installing_user": kwargs["installing_user"],
        }
        return self.db.oauth_keys.insert_one(resp)

    def key_grab(self, selector):
        return self.db.oauth_keys.find_one({"team_id": selector})

    def add_feed(self, **kwargs):
        feed = {
            "user_id": kwargs["user_id"],
            "feed_url": kwargs["feed_url"],
            "channel": kwargs["channel"],
            "workspace": kwargs["workspace"],
            "last_feed": kwargs["latest"],
        }
        return self.db.feed_list.insert_one(feed)
