import os
import os.path
import configparser
from time import sleep
from crawl.crawler import Crawler

class MainApp:
    '''This is the app entry point.It will first check if a config file exists in the current directory.
    If not,it will create a new config file and prompt the user for values'''
    def __init__(self):
        self.localDir = os.getcwd()
        self.checkforconfig(self.localDir)

    def checkforconfig(self, dir):
        filename = 'config.ini'
        filepath = os.path.join(dir, filename)
        if os.path.isfile(filepath) == True:
            """Pass the configfile for crawling"""
            print('Config file found...')
            sleep(2)
            print('Crawling has began...')
            Crawler(filepath)
        else:
            '''Create a config file here then pass for crawling'''
            print('No config file')
            sleep(2)
            print('Creating new config file with default settings...')
            config = configparser.ConfigParser()
            config['DEFAULT'] = {'StandardMedia':'http://www.standardmedia.co.ke/'}

            with open(filename,mode='w') as configfile:
                config.write(configfile)
                print('Config File created...')
            sleep(2)
            print('Crawling has began...')
            Crawler(filepath)

def run():
    MainApp()

if __name__ == '__main__':
    run()
