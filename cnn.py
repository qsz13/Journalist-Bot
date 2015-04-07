import urllib
from bs4 import BeautifulSoup
import feedparser

__author__ = 'danielqiu'


class CNN():

    feed_url = "http://rss.cnn.com/rss/edition.rss"
    news = []
    def get(self):
        items = feedparser.parse(self.feed_url).entries
        self.news = [{"title":item.title} for item in items]





