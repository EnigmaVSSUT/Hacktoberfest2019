
import datetime
import uuid
import PyRSS2Gen
import os 
n = os.path.dirname(os.path.abspath(__file__))
FEEDLOC = n+"jobstatus.rss"
DATALOC = n+"jobstatus.txt"
TITLE = "Job Status"
LINK = "Your Website Link"
DESCRIPTION = "My job statuses"



# read datefile to get the latest updates
data_file = open(DATALOC)
items = []
while 1:
    line = data_file.readline()
    if not line:
       break
    desc = line
    rss_item = PyRSS2Gen.RSSItem(
        title = "Job Status",
        link = "Link to your website",
        description = desc,
        pubDate = datetime.datetime.now(),
        guid = "Link to your website"
        )
    items.append(rss_item)


# build the rss feed
rss_feed = PyRSS2Gen.RSS2 (
    title = TITLE,
    link = LINK,
    description = DESCRIPTION,
    lastBuildDate = datetime.datetime.utcnow(),
    items = items
    )

print rss_feed.to_xml()
