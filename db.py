import os
import pymongo


db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASS')
db_uri = os.environ.get('DB_URI')


def def_example():
    try:
        client = pymongo.MongoClient(f"mongodb://{db_user}:{db_pass}@{db_uri}")

        db = client.get_database()
        main_collection = db['main_collection']
        main_collection.insert_many(SEED_DATA)
        cursor = main_collection.find({})
        for doc in cursor:
            print(doc)
        db.drop_collection('main_collection')
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
        feed_list = db['feed_list']
        feed_list.insert_one({
            'user_id': user_id,
            'feed_url': feed_url,
            'channel': channel,
            'workspace': workspace,
            'last_feed': latest
            })
        client.close()
        return f'{feed_url} successfully added'
    except:
        return f'failed to add {feed_url} to the database'
