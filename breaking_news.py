import shelve
import urllib
import time
import feedparser


__author__ = 'danielqiu'
import json


class BreakingNews():
    api_url = "http://api.breakingnews.com/api/v1/item/"
    last_update = None

    def get(self):

        d = shelve.open('breaking')
        param_dict = {}
        if self.last_update !=None:
            param_dict['date__gt'] = self.last_update

        param = urllib.urlencode(param_dict)
        url = urllib.urlopen(self.api_url + '?' + param)
        result = json.load(url)

        if len(result['objects'])>0:

            self.last_update = result['objects'][0]['date']
            news = result['objects']
            for n in news:
                content = n['content']
                importance = n['importance']
                time = n['date']
                id = str(n['id'])

                d[id] = {'content':content,'importance':importance,'time':time}








        # if self.last is not None:
        #     self.last = feedparser.parse(self.feed_url, modified=self.last.modified)
        # else:
        #     self.last = feedparser.parse(self.feed_url)
        #
        # if self.last.status != 304:
        #     print "\n\n\n\n\n\n\n"
        #     for item in self.last.entries:
        #         title = item.title
        #         time = item.updated_parsed
        #         print item




        # url = urllib.urlopen(self.api_url)
        # try:
        #
        #     result = json.load(url)
        # except Exception as e:
        #     print e
        # self.clean_data(result)
        # return self.news

    # def clean_data(self, result):
        # entries = result[u'objects']
        # self.news = []
        # for e in entries:
        #     topics = [{"name": t["name"], "category": t["category"]} for t in e["topics"]]
        #     self.news.append({"content": e['content'], "topics": topics})




def main():
    bn = BreakingNews()
    while True:
        try:

            bn.get()
            time.sleep(1)
        except Exception as e:
            print e


if __name__ == "__main__":
    main()
