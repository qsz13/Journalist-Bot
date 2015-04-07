import urllib

__author__ = 'danielqiu'
import json


class BreakingNews():
    api_url = "http://www.breakingnews.com/api/v1/item/"
    news = None

    def get(self):
        url = urllib.urlopen(self.api_url)
        result = json.load(url)
        self.clean_data(result)
        return self.news

    def clean_data(self, result):
        entries = result[u'objects']
        self.news = []
        for e in entries:
            topics = [{"name": t["name"], "category": t["category"]} for t in e["topics"]]
            self.news.append({"content": e['content'], "topics": topics})


    
