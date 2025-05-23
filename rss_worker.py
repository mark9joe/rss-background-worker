import time
import feedparser
from datetime import datetime

FEEDS = [
    "https://www.respirework.com/rss/empyrean-series.xml",
    "https://www.respirework.com/rss/rebecca-yarros.xml"
]

def fetch_and_log():
    print(f"Fetching RSS feeds at {datetime.utcnow().isoformat()} UTC")
    for url in FEEDS:
        print(f"Fetching: {url}")
        feed = feedparser.parse(url)
        if feed.entries:
            latest = feed.entries[0]
            print(f"- {latest.title} ({latest.link})")
        else:
            print("No entries found.")
    print("-" * 50)

if __name__ == "__main__":
    while True:
        fetch_and_log()
        time.sleep(1)
