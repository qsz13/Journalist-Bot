from breaking_news import BreakingNews
#from cnn import CNN
#from google_trends import GoogleTrends

__author__ = 'danielqiu'

#import socket
#import socks
#socks.set_default_proxy(socks.SOCKS5, "localhost", 1080, False)
#socket.socket = socks.socksocket





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
        pass








if __name__ == "__main__":
    main()
