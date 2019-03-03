import feedparser
import pprint
import os
from htmlslacker import HTMLSlacker

feed = ["http://www.reddit.com/r/python/.rss"]


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
            outp = parsed.entries[0].summary
            print(HTMLSlacker(outp).get_output())

        except:
            print("that didn't work")


feed_checker()