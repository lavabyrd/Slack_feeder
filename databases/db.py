import os
import pymongo
from pymongo import MongoClient


db_user = os.environ.get("DB_USER")
db_pass = os.environ.get("DB_PASS")
db_uri = os.environ.get("DB_URI")


def def_example():
    try:
        client = pymongo.MongoClient(f"mongodb://{db_user}:{db_pass}@{db_uri}")

        db = client.get_database()
        main_collection = db["main_collection"]
        main_collection.insert_many(SEED_DATA)
        cursor = main_collection.find({})
        for doc in cursor:
            print(doc)
        db.drop_collection("main_collection")
        client.close()
        print("Successfully completed and dropped")
    except:
        print("a failure occurred")


def insert_feed_url_to_db(payload, latest):
    try:
        feed_url = payload["text"]
        user_id = payload["user_id"]
        channel = payload["channel_id"]
        workspace = payload["team_id"]
        latest = latest
        client = pymongo.MongoClient(f"mongodb://{db_user}:{db_pass}@{db_uri}")
        db = client.get_database()
        feed_list = db["feed_list"]
        feed_list.insert_one(
            {
                "user_id": user_id,
                "feed_url": feed_url,
                "channel": channel,
                "workspace": workspace,
                "last_feed": latest,
            }
        )
        client.close()
        return f"{feed_url} successfully added"
    except:
        return f"failed to add {feed_url} to the database"


COLLECTION_NAME = "main_collection"


class MongoRepository(object):
    def __init__(self):
        db_user = os.environ.get("DB_USER")
        db_pass = os.environ.get("DB_PASS")
        db_uri = os.environ.get("DB_URI")

        self.db = MongoClient(f"mongodb://{db_user}:{db_pass}@{db_uri}").main_collection

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
