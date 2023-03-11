from distutils.util import execute
from scrape import Scraper
from summaryScrape import *
from cricketStats_scraper import *
from namescraper import *
import pandas as pd

def main():
    url = "https://stats.espncricinfo.com/ci/engine/player/253802.html?class=11;template=results;type=allround"

    names = getNames()
    
    # Create a second scraper to find the best batsmen of all time and run executeScraper through a list of them
    #get a list of top 100 batsmen of all time
    print( len(names))
    for name in names:
        executeScraper(url, name)

def executeScraper(url, name):
    scraper = Scraper(url, name)
    scraper.getCareerAverages()

    scrapePlayer(name)

if __name__ == '__main__':
    main()