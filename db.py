import os
import pymongo


db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASS')
db_uri = os.environ.get('DB_URI')

SEED_DATA = [
    {
        'decade': '1970s',
        'artist': 'Debby Boone',
        'song': 'You Light Up My Life',
        'weeksAtOne': 10
    },
    {
        'decade': '1980s',
        'artist': 'Olivia Newton-John',
        'song': 'Physical',
        'weeksAtOne': 10
    },
    {
        'decade': '1990s',
        'artist': 'Mariah Carey',
        'song': 'One Sweet Day',
        'weeksAtOne': 16
    }
]


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


if __name__ == "__main__":
    def_example()