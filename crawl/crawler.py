from crawl import url_manager
from crawl import outputer
from crawl import parser
from crawl import downloader
import time
import random
import os

class crawler:
    def __init__(self):
        self.urls = url_manager.manager()
        self.downloader = downloader.download(None)
        self.parser = parser.parse()
        self.outputer = outputer.output()
        self.count = 0
    def startCrawl(self, root_url, toggle_print = True):
        assert isinstance(toggle_print, bool)
        self.urls.addNewUrl(root_url)
        while not self.urls.isEmpty():
            try:
                new_url = self.urls.getUrl()
                if toggle_print:
                    print("crawling %d : %s"%(self.count, new_url))
                self.downloader.url = new_url
                html_out = self.downloader.startDownload()
                next_url, data = self.parser.startParse(new_url, html_out)
                self.urls.addNewUrl(next_url)
                self.outputer.collectData(data)
                self.count += 1
                #time.sleep(random.random() * 20)
            except: print("failed\n")
            else: print("successful\n")
        if toggle_print:
            print("\n\nfinish crawling\nwritting file...")
        path = str(os.path.dirname(os.path.abspath(__file__))) + "/sushiReview.txt"
        self.outputer.writeTXT(path)
        if toggle_print:
            print("\nfinished. file located at: %s"%path)