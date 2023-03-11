from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from summaryScrape import *

def scrapePlayer(name):
    url = 'https://stats.espncricinfo.com/ci/engine/stats/index.html?class=1;type=batting'
    s=Service('chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    driver.get(url)

    # Find the search bar and find data from selected player
    search_bar = driver.find_element(By.XPATH, value="//*[@id='ciHomeContentlhs']/div[3]/div[3]/form/input[1]")
    search_bar.send_keys(name)

    # Submit 
    search_button = driver.find_element(By.XPATH, value="//*[@id='ciHomeContentlhs']/div[3]/div[3]/form/input[2]")
    search_button.click()

    driver.find_element(By.XPATH, value='//*[@id="player"]/a').click()
    # Find test data
    #                                   //*[@id="gurusearch_player"]/table/tbody/tr[1]/td[3]/a[1]
    try:
        test_button = driver.find_element(By.XPATH, value='//*[@id="gurusearch_player"]/table/tbody/tr/td[3]/a[1]').click()
    except:
        test_button = driver.find_element(By.XPATH, value='//*[@id="gurusearch_player"]/table/tbody/tr[1]/td[3]/a[1]').click()
    #Click from drop-down for all records
    select = Select(driver.find_element(By.XPATH, value='//*[@id="ciHomeContentlhs"]/div[3]/div/div[1]/select'))
    select.select_by_visible_text('All Test/ODI/T20I')

    submit_query = driver.find_element(By.XPATH, value="//*[@id='ciHomeContentlhs']/div[3]/div/table[1]/tbody/tr/td/table/tbody/tr[2]/td/form/table/tbody/tr[11]/td[2]/table/tbody/tr/td[1]/input")
    submit_query.click()

    #Get url for the player
    url = driver.current_url
    getPlayerCareerSummary(name, url)
    #time.sleep(10)
