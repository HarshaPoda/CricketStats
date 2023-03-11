import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36", "Accept-Encoding": "gzip, deflate, br", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

def getPlayerCareerSummary(playerName, url):
    request = requests.get(url, headers=header)
    soup = BeautifulSoup(request.content, 'html.parser')

    table_data = soup.find_all("table", {'class':'engineTable'})

    # Table_Data Position 2 & 3 contain data for the records
    career_average = table_data[2]
    career_summary = table_data[3]

    #Creating DataFrame for career summary
    career_summary_columnName = []
    career_summary_data = []

    for item in career_summary.find_all("th"):
        career_summary_columnName.append(item.text)
    career_summary_columnName = career_summary_columnName[:-1]

    summary_types = ['Type', 'Against Country', 'In Country', 'In Continent', 'Home_Away', 'By Year', 'By Season', 'Under Captain', 'Cap_Not Cap', 'Not Keeper', 'If Won Toss', 'Bat_Bowl based on Choice', 'Bat_Bow first', 
    'Team Innings(1&2 or 3&4)', 'By Innings', 'Day_Night', 'Match Result', 'Result based on Bat_Bowl', '# of team series', 'Match Number in Series', 'Tournament', 'Tournament Round']

    # Create a new list for each value

    for tbody in career_summary.find_all("tbody"):
        summary_type_data = []
        for tr in tbody.find_all("tr"):
            data = []
            for td in tr.find_all("td"):
                data.append(td.text)
            if len(data) != 1:
                data = data[:-1]
                summary_type_data.append(data)
        career_summary_data.append(summary_type_data)   

    if len(career_summary_data) == 23:
        summary_types = ['Type', 'World XI' ,'Against Country', 'In Country', 'In Continent', 'Home_Away', 'By Year', 'By Season', 'Under Captain', 'Cap_Not Cap', 'Not Keeper', 'If Won Toss', 'Bat_Bowl based on Choice', 'Bat_Bow first', 
    'Team Innings(1&2 or 3&4)', 'By Innings', 'Day_Night', 'Match Result', 'Result based on Bat_Bowl', '# of team series', 'Match Number in Series', 'Tournament', 'Tournament Round']

    # Create dataframes based on different types
    summaryPd_dict = {}
    i = 0
    for item in career_summary_data:
        summaryPd_dict[summary_types[i]] = pd.DataFrame(item, columns=career_summary_columnName)
        i = i + 1

    # When writing to AWS create a new function to handle that
    #Print the data files
    playerName = playerName.replace(' ', '_')
    path = 'Data/'+playerName
    if not os.path.exists(path):
        os.makedirs(path)
        
    for item in summaryPd_dict:
        summaryPd_dict[item].to_csv(path + '/'+item+'.csv')
