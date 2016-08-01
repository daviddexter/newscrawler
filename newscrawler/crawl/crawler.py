import configparser
from crawl.bot import CrawlerBot
import concurrent.futures

URLS = []
class Crawler:
    def __init__(self,configfile):
        self.configfile = configfile
        self.listdownurls(self.configfile)

    def listdownurls(self,file):
        config = configparser.ConfigParser()
        config.read(file)
        for k in config.defaults():
            keys = config.defaults()[k]
            URLS.append(keys)
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            for url in URLS:
                executor.submit(self.pagecrawl,url)

    def pagecrawl(self,url):
        '''call the web crawler'''
        CrawlerBot(url)





