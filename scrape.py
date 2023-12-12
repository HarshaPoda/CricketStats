import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import json
header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36", "Accept-Encoding": "gzip, deflate, br", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}


class Scraper:
    def __init__( self, url, playerName ):
        self.url = url
        self.playerName = playerName

    def getUrlData(self, url):
        request = requests.get(url, headers=header)
        return BeautifulSoup(request.content, 'html.parser')

    def getDataFromScraper(self, soup):
        table_data = soup.find_all("table", {'class':'engineTable'})
        # Table_Data Position 2 & 3 contain data for the records
        career_average = table_data[2]
        career_summary = table_data[3]

        #Creating DataFrame for career average
        career_average_columnName = []
        career_average_data = []

        for item in career_average.find_all("th"):
            career_average_columnName.append(item.text)

        for item in career_average.find_all("td"):
            career_average_data.append(item.text)

        career_average_columnName = career_average_columnName[1:-1]
        career_average_data = career_average_data[1:-1]

        #Create a data frame for Career Averages
        career_average_df = pd.DataFrame( data=[career_average_data], columns=career_average_columnName)

        self.playerName = self.playerName.replace(' ', '_')
        path = 'Data/'+self.playerName
        if not os.path.exists(path):
            os.makedirs(path)
        
        career_average_df.to_csv(path + '/career.csv')

    def getCareerAverages(self):
        soup = self.getUrlData(self.url)
        self.getDataFromScraper(soup)

    #     self.df = career_average_df

    # def getCareerAverages(self):
    #     soup = self.getUrlData(self.url)
    #     return self.getDataFromScraper(soup)
