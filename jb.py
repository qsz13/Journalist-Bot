from breaking_news import BreakingNews
#from cnn import CNN
#from google_trends import GoogleTrends

__author__ = 'danielqiu'

#import socket
#import socks
#socks.set_default_proxy(socks.SOCKS5, "localhost", 1080, False)
#socket.socket = socks.socksocket


class DictDiffer(object):
    """
    Calculate the difference between two dictionaries as:
    (1) items added
    (2) items removed
    (3) keys same in both but changed values
    (4) keys same in both and unchanged values
    """
    def __init__(self, current_dict, past_dict):
        self.current_dict, self.past_dict = current_dict, past_dict
        self.set_current, self.set_past = set(current_dict.keys()), set(past_dict.keys())
        self.intersect = self.set_current.intersection(self.set_past)
    def added(self):
        return self.set_current - self.intersect 
    def removed(self):
        return self.set_past - self.intersect 
    def changed(self):
        return set(o for o in self.intersect if self.past_dict[o] != self.current_dict[o])
    def unchanged(self):
        return set(o for o in self.intersect if self.past_dict[o] == self.current_dict[o])


def main():
    #gt = GoogleTrends()
    #print gt.get()
    bn = BreakingNews()
    news =  bn.get()
    #cnn = CNN()
    #cnn.get()
    print news

    old_news = None
    while True:
	try:
            new_news = bn.get()
            diff = DictDiffer(new_news, old_news)
            a = diff.added()








if __name__ == "__main__":
    main()
