from bs4 import BeautifulSoup
from crawl.processor import Processor
from time import sleep
import requests

links = []
responses = []
class CrawlerBot:
    def __init__(self,url):
        self.url = url
        self.startcrawl(self.url)

    def startcrawl(self, url):
        try:
            #res = requests.urlopen(url)
            res = requests.get(url)
            responses.append(res.content)
            soup = BeautifulSoup(res.content, 'html.parser')
            alllinks = soup.find_all('a')
            #Processor(responses, alllinks)

            if len(alllinks) == 0:
                print('start processing responses for:', url)
                sleep(3)
                Processor(responses,links)
            else:
                for link in alllinks:
                    l = link.get('href')
                    links.append(l)
                    sleep(0.3)
                    return self.startcrawl(l)
        #except urllib.error.URLError as e:
        except requests.exceptions.RequestException:
            print('An error occurred for :', url)
            sleep(2)
            print('start processing partially retrieved response for: ', url)
            sleep(3)
            Processor(responses, links)









