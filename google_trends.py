__author__ = 'danielqiu'

import feedparser
import re


class GoogleTrends():

    def __init__(self):
        pass

    feed_url = "http://www.google.com/trends/hottrends/atom/feed"

    def get(self):
        entries = feedparser.parse(self.feed_url).entries
        trends = []
        for e in entries:
            traffic = int(re.sub(r"\D", "", e.ht_approx_traffic))
            trends.append({'title': e.title, 'traffic': traffic})
        return trends
