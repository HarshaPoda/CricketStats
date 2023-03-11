import requests
from bs4 import BeautifulSoup

def getNames():
    header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36", "Accept-Encoding": "gzip, deflate, br", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    names = []
    i = 1
    while i < 4:
        url = f"https://stats.espncricinfo.com/ci/engine/stats/index.html?class=11;page={i};template=results;type=batting"
        print(url)
        request = requests.get(url, headers=header)
        soup = BeautifulSoup(request.content, 'html.parser')


        table_data = soup.find_all("table", {'class':'engineTable'})
        career_summary = table_data[2]
        tbody = career_summary.find_all("tbody")

        tr = tbody[0]
        
        for item in tr.find_all("tr"):
            td = item.find("td")
            td = td.text.split(' ',2)
            name = td[0] + ' ' + td[1]
            names.append(name)
        i = i+1
    return names