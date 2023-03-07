from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = 'https://stats.espncricinfo.com/ci/engine/stats/index.html?class=1;type=batting'
s=Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get(url)

search_bar = driver.find_element(By.XPATH, value="//*[@id='ciHomeContentlhs']/div[3]/div[3]/form/input[1]")
search_bar.send_keys("Virat Kohli")

search_button = driver.find_element(By.XPATH, value="//*[@id='ciHomeContentlhs']/div[3]/div[3]/form/input[2]")
search_button.click()

time.sleep(100)

