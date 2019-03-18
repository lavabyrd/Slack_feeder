import feedparser
from htmlslacker import HTMLSlacker
import pprint

"""valid feed requirements

RSS:
    https://feedforall.com/rss-fields.htm

    required:
        Title
        Description
        Link (possibly optional?)

ATOM:
    https://validator.w3.org/feed/docs/atom.html#requiredFeedElements

    required:
        id: (similar to link)
        Title:
        updated:

Note:
    pubdate is optional for RSS??
"""


def test_rss_feed(feed_url):
    if 'title' in feedparser.parse(feed_url).feed:
        return f'{feed_url} is a good feed'
    else:
        return f'{feed_url} is an invalid feed. Please see <https://rss.com/rss-feed-validators/|this link> for some feed validators'


# def test_atom_feed(feed_url):
#     try:
#         print(feed_url)
        
#     return "blah"


feed = []


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