import feedparser
import pprint

feed = ["http://www.reddit.com/r/python/.rss"]


def add_feed():
    for item in feed:
        try:
            parsed = feedparser.parse(item)

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
        except:
            print("that didn't work")

