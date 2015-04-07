import urllib

__author__ = 'danielqiu'
import json


class BreakingNews():
    api_url = "http://www.breakingnews.com/api/v1/item/"
    news = []

    def get(self):
        url = urllib.urlopen(self.api_url)
        try:

            result = json.load(url)
        except Exception as e:
            print e
        self.clean_data(result)
        return self.news

    def clean_data(self, result):
        entries = result[u'objects']
        self.news = []
        for e in entries:
            topics = [{"name": t["name"], "category": t["category"]} for t in e["topics"]]
            self.news.append({"content": e['content'], "topics": topics})



