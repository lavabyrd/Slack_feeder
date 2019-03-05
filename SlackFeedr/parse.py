import feedparser
from htmlslacker import HTMLSlacker


def test_feed(feed_url):
    try:
        print(feed_url)
        print('http://feedparser.org/docs/examples/atom10.xml')
        parsed = feedparser.parse(feed_url)
        print("failed here?")
        if title in parsed.feed:
            print("invalid feed")
            return f"{title} is the title"
        else: 
            print ("failed")
            return "nope"
    except:
        print("test_field_failed")
        return "fail?"
        pass

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


feed_checker()