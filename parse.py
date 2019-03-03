import feedparser
import pprint
import os
import re

feed = ["http://www.reddit.com/r/python/.rss"]


import re

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)


def add_feed():
    for item in feed:
        try:
            feedparser.parse(item)
            
        except:
            print("no items found")
    print("successfull added all items")


def feed_checker():
    for item in feed:
        try:
            parsed = feedparser.parse(item)
            print(
                f"{parsed.feed.title} feed successfully "
                f"added from <url|{parsed.feed.link}>"
            )
            print(TAG_RE.sub('', parsed.entries[0].summary))
        except:
            print("that didn't work")


feed_checker()